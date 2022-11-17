pragma solidity >=0.4.21 < 0.7.0;

contract Bank
{
    int bal;

    constructor() public
    {
        bal = 10;
    }

    function getBalance() view public returns(int)
    {
        return bal;
    }

    function withdraw(int amt) public
    {
        if(bal<amt)
        {
            bal;
        }
        else
        {
            bal = bal - amt;
        }
    }

    function deposit(int amt) public
    {
        bal = bal + amt;
    }
}