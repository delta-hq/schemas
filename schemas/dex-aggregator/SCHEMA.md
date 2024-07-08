# DEX Aggregator Schema

Please follow the below schemas for integrating a DEX Aggregator with OpenBlock Labs.
- The schema supports multi-swapss

## Schemas

### Tokens

| Property     | Description                                             | Type   |
|--------------|---------------------------------------------------------|--------|
| protocolName | The name of the protocol this table belongs to.         | string |
| tokenAddress | The contract address of the token.                      | string |
| tokenName    | The full name of the token, from the eth_call name().   | string |
| tokenSymbol  | The symbol of the token, from the eth_call symbol().    | string |
| decimals     | The decimals name of the token, from the eth_call decimals(). | number |

### Token Snapshot

| Property        | Description                                                     | Type   |
|-----------------|-----------------------------------------------------------------|--------|
| timestamp       | The timestamp of the record.                                    | number |
| protocolName    | The name of the protocol this table belongs to.                 | string |
| tokenAddress    | The contract address of the token.                              | string |
| volumeAmount    | The cumulative volume amount of the token (in native, normalized terms). | number |
| volumeUsd       | The cumulative volume of the token in USD.                      | number |
| feesUsd         | The cumulative fees collected in USD.                           | number |
| incentiveAmount | The cumulative amount of incentives.                            | number |
| incentiveUsd    | The value of incentives in USD.                                 | number |

### Protocol Snapshot

| Property     | Description                                             | Type   |
|--------------|---------------------------------------------------------|--------|
| timestamp    | The timestamp of the record.                            | number |
| protocolName | The name of the protocol this table belongs to.         | string |
| volumeUsd    | The cumulative volume in USD.                           | number |
| feesUsd      | The cumulative fees collected in USD.                   | number |

### Trades

| Property           | Description                                                                 | Type       |
|--------------------|-----------------------------------------------------------------------------|------------|
| timestamp          | The timestamp of the trade.                                                 | number     |
| protocolName       | The name of the protocol this table belongs to.                             | string     |
| chainId            | The standard id of the chain this trade belongs to                          | number     |
| blockNumber        | The block number in which the trade occurred.                               | number     |
| transactionId      | The transaction id associated with this trade.                              | string     |
| fees               | The amount of fees (ideally in USD terms) for this trade.                   | number     |
| slippage           | (Optional) The slippage of the given trade.                                 | number     |
| userAddress        | The address of the user initiating the trade.                               | string     |
| inputTokens        | The contract address of the input token(s).                                 | [string]   |
| inputTokenAmounts  | Parallel array to inputTokens, dictating the normalized native amounts of each token traded. | [number]   |
| outputTokens       | The contract address of the output token(s).                                | [string]   |
| outputTokenAmounts | Parallel array to output, dictating the normalized native amounts of each token traded. | [number]   |
| swapAmountUsd      | The value of the swap in USD.                                               | number     |

