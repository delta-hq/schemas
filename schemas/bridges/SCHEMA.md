# Bridges Schema

Standard table definitions for bridge protocols, including pool-based, mint-based, and intent-based bridges.

## Schema

### Tokens

| Property       | Description                                     | Type   |
|----------------|-------------------------------------------------|--------|
| protocolName   | The name of the protocol.                       | string |
| tokenAddress   | The contract address of the token.              | string |
| tokenSymbol    | The symbol of the token.                        | string |
| chainId        | The blockchain ID where the token resides.      | number |

### Pools

| Property             | Description                                                  | Type   |
|----------------------|--------------------------------------------------------------|--------|
| creationTimestamp    | The timestamp this pool was created.                         | number |
| creationBlockNumber  | The block number this pool was created on.                   | number |
| protocolName         | The name of the protocol.                                    | string |
| token0Address        | The contract address of token 0 (in a pool based bridge). Use this as the tokenAddress for an intent-based bridge. | string |
| token0Symbol         | The symbol of token 0.                                       | string |
| token1Address        | (Optional, only applicable to pool-based) The contract address of token 1. | string |
| token1Symbol         | The symbol of token 1.                                       | string |
| feeRate              | The fee rate as a percentage for the pool, if applicable (ie, 2.3% fee as 2.3). | number |
| poolAddress          | The contract address of the pool.                            | string |
| chainId              | Standard chain ID (ie, the chain ID of the network the pool lives on). | number |
| bridgeType           | The type of bridge (ie, pool-based, mint-based, or intent-based). | string |

### LP Snapshot

| Property       | Description                                                      | Type   |
|----------------|------------------------------------------------------------------|--------|
| timestamp      | The timestamp of the snapshot.                                    | number |
| protocolName   | The name of the protocol.                                         | string |
| poolAddress    | The address of the pool.                                          | string |
| lpAddress      | The address of the liquidity provider.                            | string |
| token0Address  | The contract address of token 0.                                  | string |
| token0Amount   | The amount of token 0, decimal normalized.                        | number |
| token1Address  | The contract address of token 1.                                  | string |
| token1Amount   | The amount of token 1, decimal normalized.                        | number |
| tvlUsd         | The total value locked in USD.                                    | number |
| chainId        | The standard chain ID where the liquidity provider resides.       | number |
| bridgeType     | The type of bridge (pool-based, mint-based, or intent-based).     | string |

### User Snapshot

| Property       | Description                                                      | Type   |
|----------------|------------------------------------------------------------------|--------|
| timestamp      | The timestamp of the snapshot.                                    | number |
| protocolName   | The name of the protocol.                                         | string |
| poolAddress    | (Optional, only applicable to pool-based) The contract address of the pool. | string |
| userAddress    | The address of the user this snapshot activity is based on.       | string |
| amountInUsd    | The amount of tokens received on this network by the user in USD during the given snapshot. | number |
| amountOutUsd   | The amount of tokens sent out of this network by the user in USD during the given snapshot. | number |
| chainId        | The standard chain ID where the bridger resides.                   | number |
| bridgeType     | The type of bridge (pool-based, mint-based, or intent-based).     | string |

### Pool Snapshot

| Property       | Description                                                      | Type   |
|----------------|------------------------------------------------------------------|--------|
| timestamp      | The timestamp of the snapshot.                                    | number |
| protocolName   | The name of the protocol.                                         | string |
| poolAddress    | The contract address of the pool.                                  | string |
| token0Address  | (Optional, only applicable to pool-based) The contract address of token 0. | string |
| token0Amount   | The amount of token 0, decimal normalized.                        | number |
| token1Address  | The contract address of token 1.                                  | string |
| token1Amount   | The amount of token 1, decimal normalized.                        | number |
| tvlUsd         | The total value locked in USD, at this snapshot.                  | number |
| volumeUsd      | The bridged volume in USD, during this snapshot.                  | number |
| feesUsd        | The fees collected in USD, during the snapshot period.            | number |
| incentiveAmount| The amount of incentives given out during this snapshot period, decimal normalized. | number |
| incentiveUsd   | The value of incentives in USD.                                   | number |
| chainId        | The standard chain ID where the pool resides.                     | number |
| bridgeType     | The type of bridge (pool-based, mint-based, or intent-based).     | string |

### Protocol Snapshot

| Property       | Description                                                      | Type   |
|----------------|------------------------------------------------------------------|--------|
| timestamp      | The timestamp of the snapshot.                                    | number |
| protocolName   | The name of the protocol.                                         | string |
| tvlUsd         | (Optional, not applicable to intent-based bridges) The total value locked in USD, at this snapshot. | number |
| volumeUsd      | The volume in USD, during this given snapshot period.             | number |
| feesUsd        | The fees collected in USD, during the snapshot period.            | number |
| chainId        | The standard chain ID where the protocol resides.                 | number |
| bridgeType     | The type of bridge (pool-based, mint-based, or intent-based).     | string |

### Bridge Transactions

| Property           | Description                                                      | Type   |
|--------------------|------------------------------------------------------------------|--------|
| timestamp          | The timestamp of the transaction.                                 | number |
| blockNumber        | The block number of the transaction.                              | number |
| transactionHash    | The hash of the transaction this bridge originated from.          | string |
| protocolName       | The name of the protocol.                                         | string |
| sourceChainId      | The source standard chain ID.                                     | number |
| destinationChainId | The destination standard chain ID.                                | number |
| volumeUsd          | The volume of the transaction in USD.                             | number |
| userAddress        | The address of the user initiating the transaction.               | string |
| solverAddress      | The address of the solver (for intent-based bridges).             | string |
| poolAddress        | The address of the pool (for pool-based and mint-based bridges).  | string |
| bridgeType         | The type of bridge (pool-based, mint-based, or intent-based).     | string |

### Maker Snapshot

| Property       | Description                                                      | Type   |
|----------------|------------------------------------------------------------------|--------|
| timestamp      | The timestamp of the snapshot.                                    | number |
| protocolName   | The name of the protocol.                                         | string |
| userAddress    | The address of the maker.                                         | string |
| amountInUsd    | The amount received in USD, during this snapshot.                 | number |
| amountOutUsd   | The amount sent in USD, during this given snapshot.               | number |
| feesUsd        | The fees collected in USD, during this snapshot.                  | number |
| chainId        | The standard chain ID where the maker resides.                    | number |

### Taker Snapshot

| Property       | Description                                                      | Type   |
|----------------|------------------------------------------------------------------|--------|
| timestamp      | The timestamp of the record.                                      | number |
| protocolName   | The name of the protocol.                                         | string |
| userAddress    | The address of the taker.                                         | string |
| volumeUsd      | The volume bridged in USD, in the given snapshot.                 | number |
| chainId        | The standard chain ID where the taker resides.                    | number |

### Token Snapshot

| Property       | Description                                                      | Type   |
|----------------|------------------------------------------------------------------|--------|
| timestamp      | The timestamp of the snapshot.                                    | number |
| protocolName   | The name of the protocol.                                         | string |
| tokenAddress   | The contract address of the token.                                | string |
| volumeUsd      | The volume in USD, during the given period.                       | number |
| feesUsd        | The fees collected in USD, during this given period.              | number |
| chainId        | The standard chain ID where the token resides.                    | number |
