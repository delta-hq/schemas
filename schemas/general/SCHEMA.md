# General Schema

Table definitions for the generic schema. These tables can be used for any protocol.

## Schema

### Incentive Claim Data

| Property              | Description                                                     | Type   |
|-----------------------|-----------------------------------------------------------------|--------|
| timestamp             | The timestamp of the claim.                                     | number |
| chain_id              | The standard chain id.                                          | number |
| user_address          | The address of the user who claimed the incentives.             | string |
| claimed_token_address | The smart contract address of the claimed token.                | string |
| claimed_token_amount  | The amount of the token claimed, decimal normalized.            | number |
| claimed_token_usd     | The amount of claimed tokens in USD.                            | number |
| other_incentive_usd   | Any incentives outside of the claimed token, in this transaction, summed up in USD terms. | number |

### Airdrop

| Property                        | Description                                                     | Type   |
|---------------------------------|-----------------------------------------------------------------|--------|
| airdrop_timestamp               | The timestamp the airdrop was given to the user.                | number |
| user_address                    | The address of the user claiming the airdrop.                   | string |
| claim_timestamp                 | The timestamp of when the user claimed the airdrop.             | number |
| airdrop_token_address           | The smart contract address of the airdropped token.             | string |
| airdrop_token_symbol            | The symbol of the token being airdropped.                       | string |
| token_amounts                   | The amount of each token airdropped, decimal normalized.        | [number] |
| amount_usd                      | The USD value of the airdropped tokens.                         | number |
| first_outgoing_transaction_address | The address of the first receiver of airdropped tokens.      | string |
| first_outgoing_transaction_timestamp | The timestamp of the first outgoing transaction.          | number |
| first_outgoing_transaction_amount | The amount of the first outgoing transaction, decimal normalized. | number |
| signature                      | The signature of the airdrop.                                    | string |
| method_id                      | The method ID of the airdrop.                                    | string |

### User Liquidity Snapshot

| Property          | Description                                                     | Type   |
|-------------------|-----------------------------------------------------------------|--------|
| timestamp         | The timestamp of the snapshot.                                   | number |
| chain_id          | The standard chain id.                                           | number |
| user_address      | The address of the user.                                         | string |
| token_address     | The smart contract address of the token.                         | string |
| token_symbol      | The symbol of the token.                                         | string |
| token_amount      | The amount of the token, decimal normalized.                     | number |
| token_amount_usd  | The USD value of the token.                                      | number |

### Pool Snapshot

| Property          | Description                                                     | Type   |
|-------------------|-----------------------------------------------------------------|--------|
| timestamp         | The timestamp of the record.                                     | number |
| chain_id          | The standard chain id.                                           | number |
| protocol_type     | The type of protocol (ie, Lending, CDP, DEX, Gaming, etc).       | string |
| pool_address      | The smart contract address of the pool.                          | string |
| pool_name         | The name of the pool (ie, pool() in the smart contract, if it exists). | string |
| total_value_locked_usd | The total value locked within this pool in USD.             | number |
| return_30d        | The return of this pool over 30 days.                            | number |
| supply_apr        | The annual percentage rate of this pool at the snapshot.         | number |
| supply_apy        | The annual percentage yield of the pool.                         | number |

### User Transaction Snapshot

| Property          | Description                                                     | Type   |
|-------------------|-----------------------------------------------------------------|--------|
| timestamp         | The timestamp of the snapshot.                                   | number |
| chain_id          | The standard chain id.                                           | number |
| user_address      | The address of the user.                                         | string |
| transaction_count | Number of transactions during this snapshot period from the user.| number |
| transaction_fees  | The amount of fees in this given period, decimal normalized.     | number |
