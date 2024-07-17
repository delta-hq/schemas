# DEX Aggregator Schema

Please follow the below schemas for integrating a DEX Aggregator with OpenBlock Labs.
- The schema supports multi-swaps

## Schemas

### Tokens
| Property      | Description                                             | Type   |
|---------------|---------------------------------------------------------|--------|
| protocolName  | The name of the protocol.                               | string |
| chainId       | The standard id of the chain.                           | number |
| tokenAddress  | The contract address of the token.                      | string |
| tokenName     | The full name of the token, from the eth_call name().   | string |
| tokenSymbol   | The symbol of the token, from the eth_call symbol().    | string |
| decimals      | The decimals name of the token, from the eth_call decimals().| number |

### Token Snapshot
| Property        | Description                                                      | Type   |
|-----------------|------------------------------------------------------------------|--------|
| timestamp       | The timestamp of the record.                                     | number |
| protocolName    | The name of the protocol this table belongs to.                  | string |
| chainId         | The standard id of the chain.                                    | number |
| tokenAddress    | The contract address of the token.                               | string |
| volumeAmount    | The volume amount of the token, during the snapshot period, decimal normalized. | number |
| volumeUsd       | The volume of the token in USD.                                  | number |
| fees            | The fees (ie, revenue generated from trading this token) from this token in native, decimal normalized terms. | number |
| feesUsd         | The fees collected in USD.                                       | number |
| incentiveAmount | The amount of incentives collected from this token, during the snapshot period, decimal normalized. | number |
| incentiveUsd    | The value of incentives in USD.                                  | number |

### Protocol Snapshot
| Property      | Description                                                           | Type   |
|---------------|-----------------------------------------------------------------------|--------|
| timestamp     | The timestamp of the block this snapshot was taken.                   | number |
| protocolName  | The name of the protocol.                                             | string |
| chainId       | The standard id of the chain.                                         | number |
| volumeUsd     | The volume in USD, in the given snapshot period.                      | number |
| feesUsd       | The fees (ie, total revenue generated in the protocol) collected in USD, during the snapshot period. | number |

### Trades
| Property           | Description                                                                 | Type    |
|--------------------|-----------------------------------------------------------------------------|---------|
| timestamp          | The timestamp of the trade.                                                 | number  |
| protocolName       | The name of the protocol this table belongs to.                             | string  |
| chainId            | The standard id of the chain this trade belongs to.                         | number  |
| blockNumber        | The block number in which the trade occurred.                               | number  |
| transactionId      | The transaction id associated with this trade.                              | string  |
| fees               | The amount of fees from this trade (ie, the revenue generated from executing this trade). | number  |
| feesUsd            | The fees for this trade in USD.                                             | number  |
| slippage           | (Optional) The slippage of the given trade, as a percentage (ie, 0.3% slippage is 0.3). | number  |
| userAddress        | The address of the user initiating the trade.                               | string  |
| inputTokens        | The contract address of the input token(s).                                 | [string]|
| inputTokenAmounts  | Parallel array to inputTokens, dictating the normalized native amounts of each token traded. | [number]|
| outputTokens       | The contract address of the output token(s).                                | [string]|
| outputTokenAmounts | Parallel array to output, dictating the normalized native amounts of each token traded. | [number]|
| swapAmountUsd      | The value of the swap in USD.                                               | number  |
