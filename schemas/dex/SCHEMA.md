# DEX Schema

This is OpenBlock Labs standard DEX schema.

## Schema

### Pools
| Property            | Description                                                          | Type   |
|---------------------|----------------------------------------------------------------------|--------|
| protocolName        | The name of the protocol this table belongs to.                      | string |
| chainId             | The standard id of the chain.                                        | number |
| creationBlockNumber | The block this pool was created in.                                  | number |
| creationTimestamp   | The timestamp of the block that this pool was created in.            | number |
| poolAddress         | The contract address of the lp pool.                                 | string |
| lpTokenAddress      | The token address of the LP token for this pool.                     | string |
| lpTokenSymbol       | The symbol of the LP token.                                          | string |
| tokenAddress        | The token address of the pool token at tokenIndex.                   | string |
| tokenIndex          | The index in the pool smart contract that this token appears at.     | number |
| feeRate             | The fee rate of the pool.                                            | number |
| dexType             | The type of the DEX (e.g., CPMM, CLMM, Orderbook).                   | string |

### LP Position Snapshot
| Property            | Description                                                          | Type   |
|---------------------|----------------------------------------------------------------------|--------|
| timestamp           | The timestamp of the snapshot.                                       | number |
| protocolName        | The name of the protocol this table belongs to.                      | string |
| chainId             | The standard id of the chain.                                        | number |
| poolAddress         | The contract address of the pool.                                    | string |
| lpAddress           | The address of the liquidity provider.                               | string |
| tokenIndex          | The token index based on the smart contract.                         | number |
| lpTokenAddress      | The contract address of the LP token.                                | string |
| lpTokenSymbol       | The symbol of the LP token.                                          | string |
| lpTokenAmount       | The amount of the LP token held by the liquidity provider.           | number |
| lpTokenAmountUsd    | The amount of the LP token in USD.                                   | number |
| feesUsd             | LP fees paid in the given period, in USD.                            | number |
| incentiveAmount     | The amount of incentives given out over the snapshot period, in USD. | number |
| incentiveUsd        | The incentives in USD.                                               | number |

### Pool Snapshot
| Property            | Description                                                          | Type   |
|---------------------|----------------------------------------------------------------------|--------|
| timestamp           | The timestamp of the snapshot.                                       | number |
| protocolName        | The name of the protocol this table belongs to.                      | string |
| chainId             | The standard id of the chain.                                        | number |
| poolAddress         | The contract address of the LP pool.                                 | string |
| tokenIndex          | The token index in the smart contract.                               | number |
| tokenAddress        | The contract address of the token in the pool.                       | string |
| tokenSymbol         | The symbol of the token.                                             | string |
| tokenAmount         | The amount of the token in this pool at the snapshot.                | number |
| tokenAmountUsd      | The amount of the token in USD.                                      | number |
| poolVolumeUsd       | The volume of the pool in USD, during the snapshot period.           | number |
| poolFeesUsd         | The fees of the pool in USD, during the snapshot.                    | number |
| poolIncentiveAmount | The amount of incentives in the pool, during the snapshot.           | number |
| poolIncentiveUsd    | The value of incentives in the pool in USD.                          | number |

### Protocol Snapshot
| Property            | Description                                                          | Type   |
|---------------------|----------------------------------------------------------------------|--------|
| timestamp           | The timestamp of the snapshot.                                       | string |
| protocolName        | The name of the protocol this table belongs to.                      | string |
| chainId             | The standard id of the chain.                                        | number |
| tvlUsd              | The total value locked in USD.                                       | number |
| volumeUsd           | The volume in USD.                                                   | number |
| feesUsd             | The fees collected in USD.                                           | number |

### Trades
| Property            | Description                                                          | Type   |
|---------------------|----------------------------------------------------------------------|--------|
| timestamp           | The timestamp of the transaction.                                    | number |
| chainId             | The standard id of the chain.                                        | number |
| blockNumber         | The block number of the trade.                                       | number |
| logIndex            | The log index of the event recorded.                                 | number |
| transactionHash     | The hash of the transaction.                                         | string |
| pairName            | The name of the token pair.                                          | string |
| poolAddress         | The contract address of the LP pool being traded in.                 | string |
| inputTokenSymbol    | The symbol of the input token.                                       | string |
| inputTokenAddress   | The contract address of the input token.                             | string |
| inputTokenAmount    | The amount of the input token, decimal normalized.                   | number |
| outputTokenSymbol   | The symbol of the output token.                                      | string |
| outputTokenAddress  | The contract address of the output token.                            | string |
| outputTokenAmount   | The amount of the output token, decimal normalized.                  | number |
| swapAmountUsd       | The amount of the swap in USD.                                       | number |
| feeUsd              | The fee for the trade in USD.                                        | number |

### Mints
| Property            | Description                                                          | Type   |
|---------------------|----------------------------------------------------------------------|--------|
| timestamp           | The timestamp of the record.                                         | number |
| protocolName        | The name of the protocol this table belongs to.                      | string |
| chainId             | The standard id of the chain.                                        | number |
| blockNumber         | The block number of the mint.                                        | number |
| userAddress         | The address of the user who initiated this event.                    | string |
| poolAddress         | The contract address of the pool.                                    | string |
| token0Address       | The contract address of token0.                                      | string |
| token0Amount        | The amount of token0.                                                | number |
| token1Address       | The contract address of token1.                                      | string |
| token1Amount        | The amount of token1.                                                | number |
| mintAmount          | The amount of LP token minted by the trader, decimal normalized.     | number |
| mintAmountUsd       | The amount of the mint in USD.                                       | number |

### Burns
| Property            | Description                                                          | Type   |
|---------------------|----------------------------------------------------------------------|--------|
| timestamp           | The timestamp of the record.                                         | number |
| protocolName        | The name of the protocol this table belongs to.                      | string |
| chainId             | The standard id of the chain.                                        | number |
| blockNumber         | The block number of the burn.                                        | number |
| userAddress         | The address of the user who initiated this event.                    | string |
| poolAddress         | The contract address of the pool.                                    | string |
| token0Address       | The contract address of token0.                                      | string |
| token0Amount        | The amount of token0.                                                | number |
| token1Address       | The contract address of token1.                                      | string |
| token1Amount        | The amount of token1.                                                | number |
| burnAmount          | The amount of LP tokens burned, decimal normalized.                  | number |
| burnAmountUsd       | The amount of the burn in USD.                                       | number |

### Syncs
| Property            | Description                                                          | Type   |
|---------------------|----------------------------------------------------------------------|--------|
| timestamp           | The timestamp of the record.                                         | number |
| protocolName        | The name of the protocol this table belongs to.                      | string |
| chainId             | The standard id of the chain.                                        | number |
| blockNumber         | The block number of the sync.                                        | number |
| poolAddress         | The contract address of the pool.                                    | string |
| token0Address       | The contract address of token0.                                      | string |
| token0Amount        | The amount of token0.                                                | number |
| token1Address       | The contract address of token1.                                      | string |
| token1Amount        | The amount of token1.                                                | number |

### Transfers
| Property            | Description                                                          | Type   |
|---------------------|----------------------------------------------------------------------|--------|
| timestamp           | The timestamp of the record.                                         | number |
| protocolName        | The name of the protocol this table belongs to.                      | string |
| chainId             | The standard id of the chain.                                        | number |
| blockNumber         | The block number of the transfer.                                    | number |
| userAddress         | The address of the user who initiated this event.                    | string |
| poolAddress         | The contract address of the pool.                                    | string |
| poolTokenBalance    | The balance of the pool token, decimal normalized.                   | number |

### V3 Events
| Property            | Description                                                          | Type   |
|---------------------|----------------------------------------------------------------------|--------|
| timestamp           | The timestamp of the record.                                         | number |
| protocolName        | The name of the protocol this table belongs to.                      | string |
| chainId             | The standard id of the chain.                                        | number |
| blockNumber         | The block number of the activity.                                    | number |
| eventType           | The action taken (e
