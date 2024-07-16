# Yield Aggregators Schema

This is OpenBlock Labs standard Yield Aggregators schema.

## Schema

### Pools
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| protocolName          | The name of the protocol.                                            | string |
| chainId               | The standard chain id.                                               | number |
| creationTimestamp     | The timestamp this pool was created.                                 | number |
| creationBlockNumber   | The block number that this pool was created.                         | number |
| underlyingTokenAddress| The contract address of the underlying token or deposited token.     | string |
| underlyingTokenSymbol | The symbol of the underlying token token.                            | string |
| receiptTokenAddress   | The contract address of the output or receipt token of this pool, if available.| string |
| receiptTokenSymbol    | The symbol of the receipt token.                                     | string |
| poolAddress           | The smart contract address of the pool.                              | string |
| poolSymbol            | The symbol of the pool.                                              | string |

### Position Snapshot
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| timestamp             | The timestamp of the snapshot.                                       | number |
| protocolName          | The name of the protocol.                                            | string |
| chainId               | The standard chain id.                                               | number |
| poolAddress           | The address of the pool this user has a position in.                 | string |
| userAddress           | The address of the user who has a position in the pool.              | string |
| depositAmount         | The amount of the underlying token that the user deposited, decimal normalized.| number |
| depositAmountUsd      | The deposit amount in USD.                                           | number |
| feesUsd               | The total fees in USD for the given snapshot period.                 | number |
| incentiveAmount       | The amount of incentives.                                            | number |
| incentiveUsd          | The value of incentives in USD.                                      | number |

### Pool Snapshot
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| timestamp             | The timestamp of the snapshot.                                       | number |
| protocolName          | The name of the protocol.                                            | string |
| chainId               | The standard chain id.                                               | number |
| poolAddress           | The address of the pool.                                             | string |
| depositAmount         | The amount of underlying token deposited in this pool, decimal normalized.| number |
| depositAmountUsd      | The total value locked in this pool of the deposited token in USD.   | number |
| feesUsd               | The fees in this pool in USD for the given snapshot period.          | number |
| incentiveTokenAddress | The contract address of the incentive token, if available.           | string |
| incentiveAmount       | The amount of incentives given out in the snapshot period, decimal normalized.| number |
| incentiveUsd          | The value of incentives given out in USD.                            | number |

### Protocol Snapshot
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| timestamp             | The timestamp of the snapshot.                                       | number |
| protocolName          | The name of the protocol.                                            | string |
| chainId               | The standard chain id.                                               | number |
| tvlUsd                | The total value locked in USD.                                       | number |
| feesUsd               | The fees in USD.                                                     | number |
