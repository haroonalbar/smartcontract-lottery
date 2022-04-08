// SPDX-License-Identifier: MIT

pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract Lottery is VRFConsumerBase, Ownable {
    address payable[] public players;
    uint256 usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;

    enum LOTTERY_STATE {
        CLOSED,
        OPEN,
        PROCESSING_WINNER
    }
    // 0 , 1 ,2
    LOTTERY_STATE public lottery_state;
    uint256 public fee;
    bytes32 public keyhash;

    constructor(
        address _priceFeedAddress,
        address _vrfCoordinator,
        address _link,
        uint256 _fee,
        bytes32 _keyhash
    ) public VRFConsumerBase(_vrfCoordinator, _link) {
        usdEntryFee = 50 * (10**18);
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
        lottery_state = LOTTERY_STATE.CLOSED;
        fee = _fee;
        keyhash = _keyhash;
    }

    function enter() public payable {
        //min 50 usd
        require(lottery_state == LOTTERY_STATE.OPEN);
        require(msg.value >= getEntranceFee(), "Not enough ETH!");
        players.push(msg.sender);
    }

    function getEntranceFee() public view returns (uint256) {
        require(lottery_state == LOTTERY_STATE.CLOSED);

        (, int256 price, , , ) = ethUsdPriceFeed.latestRoundData();

        uint256 adjustedPrice = uint256(price) * 10**10; //made it equlavalnt to wei
        uint256 costToEnter = (usdEntryFee * 10**18) / adjustedPrice;
        return costToEnter;
    }

    function startLottery() public onlyOwner {
        require(
            lottery_state == LOTTERY_STATE.CLOSED,
            "Can't start a new lottery yet"
        );
        lottery_state = LOTTERY_STATE.OPEN;
    }

    function endLottery() public onlyOwner {
        //uint256(keccak256(abi.encodePacked(nonce,msg.sender,block.difficulty,block.timestamp)))%players.length;
        lottery_state = LOTTERY_STATE.PROCESSING_WINNER;
        bytes32 requestId = requestRandomness(keyhash, fee);
    }
}
