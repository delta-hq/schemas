# General

Table definitions for the generic schema. These tables can be used for any protocol.

## Version: 1.0.0-alpha

### Incentive Claim Data

Transactional data on user level incentives claimed data.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the claim.                               | number |
| chain_id                 | The standard chain id.                                    | number |
| transaction_hash         | The hash of the transaction.                              | string |
| log_index                | The log index of the event recorded.                      | number |
| user_address             | The address of the user who claimed the incentives.       | string |
| claimed_token_address    | The smart contract address of the claimed token.          | string |
| claimed_token_amount     | The amount of the token claimed, decimal normalized.      | number |
| claimed_token_usd        | The amount of claimed tokens in USD.                      | number |
| other_incentive_usd      | Any incentives outside of the claimed token, in this transaction, summed up in USD terms. | number |

### Airdrop

Schema for airdrop data.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| airdrop_timestamp        | The timestamp the airdrop was given to the user.          | number |
| user_address             | The address of the user claiming the airdrop.             | string |
| claim_timestamp          | The timestamp of when the user claimed the airdrop.       | number |
| transaction_hash         | The hash of the transaction.                              | string |
| log_index                | The log index of the event recorded.                      | number |
| airdrop_token_address    | The smart contract address of the airdropped token.       | string |
| airdrop_token_symbol     | The symbol of the token being airdropped.                 | string |
| token_amount             | The amount of each token airdropped, decimal normalized.  | number |
| amount_usd               | The USD value of the airdropped tokens.                   | number |

### Pool Snapshot

APR and APY data at the pool level.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the record.                              | number |
| chain_id                 | The standard chain id.                                    | number |
| protocol_type            | The type of protocol (ie, Lending, CDP, DEX, Gaming, etc). | string |
| pool_address             | The smart contract address of the pool.                   | string |
| pool_name                | The name of the pool (ie, pool() in the smart contract, if it exists). | string |
| total_value_locked_usd   | The total value locked within this pool in USD.           | number |
| supply_apr               | The annual percentage rate of this pool at the snapshot.  | number |
| supply_apy               | The annual percentage yield of the pool.                  | number |

### Protocol Snapshot

Protocol level snapshot focused on incentives and users.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| chain_id                 | The standard chain id.                                    | number |
| daily_active_users       | The number of unique daily active users on this protocol. | number |
| transaction_count        | The number of transactions in this time period.           | number |
| fees_usd                 | The amount of fees in this given period, decimal normalized. | number |

> Note: This markdown file is auto-generated.
