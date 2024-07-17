# General Schema

Table definitions for the generic schema. These tables can be used for any protocol.

## Schema

### Incentive Claim Data

| Property             | Description                                                     | Type   |
|----------------------|-----------------------------------------------------------------|--------|
| timestamp            | The timestamp of the claim.                                     | number |
| protocolName         | The name of the protocol.                                       | string |
| chainId              | The standard chain id.                                          | number |
| userAddress          | The address of the user.                                        | string |
| claimedTokenAddress  | The smart contract address of the claimed token.                |        |
| claimedTokenAmount   | The amount of the token claimed, decimal normalized.             | number |
| claimedTokenUsd      | The amount of claimed tokens in USD.                             | number |
| otherIncentiveUsd    | Any incentives outside of the claimed token, in this transaction, summed up in USD terms. | number |

### Airdrop

| Property                        | Description                                                     | Type   |
|---------------------------------|-----------------------------------------------------------------|--------|
| airdropTimestamp                | The timestamp the airdrop was given to the user.                 | number |
| userAddress                     | The address of the user claiming the airdrop.                    | string |
| claimTimestamp                  | The timestamp of when the user claimed the airdrop.              | number |
| airdropTokenAddress             | The smart contract address of the airdropped token.              | string |
| airdropTokenSymbol              | The symbol of the token being airdropped.                        | string |
| tokenAmounts                    | The amount of each token airdropped, decimal normalized.         | [number] |
| amountUsd                       | The USD value of the airdropped tokens.                          | number |
| firstOutgoingTransactionAddress | The address of the first receiver of airdropped tokens.          | string |
| firstOutgoingTransactionTimestamp | The timestamp of the first outgoing transaction.               | number |
| firstOutgoingTransactionAmount  | The amount of the first outgoing transaction, decimal normalized. | number |
| signature                       | The signature of the airdrop.                                   | string |
| methodId                        | The method ID of the airdrop.                                   | string |

### Protocol Snapshot

| Property          | Description                                                     | Type   |
|-------------------|-----------------------------------------------------------------|--------|
| timestamp         | The timestamp of the snapshot.                                   | number |
| protocolName      | The name of the protocol.                                        | string |
| chainId           | The standard chain id.                                           | number |
| dailyActiveUsers  | The number of unique daily active users on this protocol.        | number |
| transactionCount  | The number of transactions in this time period.                  | number |
| transactionFees   | The amount of fees in this given period, decimal normalized.     | number |
| incentiveAmount   | The amount of incentives given out over the snapshot period, decimal normalized. | number |
| incentiveUsd      | The value of incentives in USD.                                  | number |

### User Liquidity Snapshot

| Property          | Description                                                     | Type   |
|-------------------|-----------------------------------------------------------------|--------|
| timestamp         | The timestamp of the snapshot.                                   | number |
| protocolName      | The name of the protocol.                                        | string |
| chainId           | The standard chain id.                                           | number |
| userAddress       | The address of the user.                                         | string |
| tokenAddress      | The smart contract address of the token.                         |        |
| tokenSymbol       | The symbol of the token.                                         | string |
| tokenAmount       | The amount of the token, decimal normalized.                     | number |
| tokenAmountUsd    | The USD value of the token.                                      | number |

### Pool Snapshot

| Property          | Description                                                     | Type   |
|-------------------|-----------------------------------------------------------------|--------|
| timestamp         | The timestamp of the record.                                     | number |
| protocolName      | The name of the protocol.                                        | string |
| chainId           | The standard chain id.                                           | number |
| protocolType      | The type of protocol (ie, Lending, CDP, DEX, Gaming, etc).       | string |
| poolAddress       | The smart contract address of the pool.                          | string |
| poolName          | The name of the pool (ie, pool() in the smart contract, if it exists). | string |
| tvlUsd            | The total value locked within this pool in USD.                  | number |
| return30d         | The return of this pool over 30 days.                            | number |
| apr               | The annual percentage rate of this pool at the snapshot.         | number |
| apy               | The annual percentage yield of the pool.                         | number |

### User Transaction Snapshot

| Property          | Description                                                     | Type   |
|-------------------|-----------------------------------------------------------------|--------|
| timestamp         | The timestamp of the snapshot.                                   | number |
| protocolName      | The name of the protocol.                                        | string |
| chainId           | The standard chain id.                                           | number |
| userAddress       | The address of the user.                                         | string |
| transactionCount  | Number of transactions during this snapshot period from the user.| number |
| transactionFees   | The amount of fees in this given period, decimal normalized.     | number |
