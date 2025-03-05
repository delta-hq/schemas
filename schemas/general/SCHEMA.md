# General

Table definitions for the generic schema. These tables can be used for any protocol.

## Version: 1.0.0-alpha

### Incentive Claim Data

Pool level allocations for an incentive program period.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the claim.                               | timestamp |
| chain_id                 | The standard chain id.                                    | int |
| transaction_hash         | The hash of the transaction.                              | string |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_signer       | The address of the account that signed the transaction.   | string |
| user_address             | The address of the user who claimed the incentives (could be different from the transaction_signer). | string |
| claimed_token_address    | The smart contract address of the claimed token.          | string |
| amount                   | The amount of the token claimed, decimal normalized.      | double |
| amount_usd               | The amount of claimed tokens in USD.                      | double |
| other_incentive_usd      | (Optional) Any incentives outside of the claimed token, in this transaction, summed up in USD terms. | double |

### Pool Level Incentive Allocations

Transactional data on user level incentives claimed data.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| reward_token             | The token address used to provide reward incentives.      | string |
| token_symbol             | The token symbol used to provide reward incentives.       | string |
| amount                   | The amount of incentives provided over the period.        | double |
| start_timestamp          | The starting timestamp of the incentive period.           | timestamp |
| end_timestamp            | The ending timestamp of the incentive period.             | timestamp |
| protocol_category        | The category of the protocol (DEX, Lending, etc...).      | string |
| protocol_name            | The name of the protocol receiving incentives.            | string |
| pool_address             | The address of the pool receiving incentives.             | string |
| reward_hash              | The transaction hash of the rewards (if applicable).      | string |
| log_index                | The log index for the event in the rewards transaction (if applicable). | int |
| submission_timestamp     | The timestamp of reward submissions.                      | timestamp |
| chain_id                 | The standard chain id.                                    | int |
| program_name             | The name of the program providing incentives.             | string |

### Airdrop

Schema for airdrop data.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| airdrop_timestamp        | The timestamp the airdrop was given to the user.          | timestamp |
| user_address             | The address of the user claiming the airdrop.             | string |
| claim_timestamp          | The timestamp of when the user claimed the airdrop.       | timestamp |
| transaction_hash         | The hash of the transaction.                              | string |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| airdrop_token_address    | The smart contract address of the airdropped token.       | string |
| airdrop_token_symbol     | The symbol of the token being airdropped.                 | string |
| token_amount             | The amount of each token airdropped, decimal normalized.  | double |
| amount_usd               | The USD value of the airdropped tokens.                   | double |

### Pool Snapshot

APR and APY data at the pool level.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the record.                              | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard chain id.                                    | int |
| protocol_type            | The type of protocol (ie, Lending, CDP, DEX, Gaming, etc). | string |
| pool_address             | The smart contract address of the pool.                   | string |
| pool_name                | The name of the pool (ie, pool() in the smart contract, if it exists). | string |
| total_value_locked_usd   | The total value locked within this pool in USD.           | double |
| supply_apr               | The annual percentage rate of this pool at the snapshot.  | double |
| supply_apy               | The annual percentage yield of the pool.                  | double |

### Protocol Snapshot

Protocol level snapshot focused on incentives and users.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard chain id.                                    | int |
| daily_active_users       | The number of unique daily active users on this protocol. | bigint |
| transaction_count        | The number of transactions in this time period.           | bigint |
| fees_usd                 | The amount of fees in this given period, decimal normalized. | double |

### Token Balance Snapshot

User level token balance snapshots.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard chain id.                                    | int |
| user_address             | The address of the user this snapshot activity is based on. | string |
| token_address            | The smart contract address of the token.                  | string |
| token_symbol             | The symbol of the token we are getting the balance of.    | string |
| token_amount             | The amount of the token at the given snapshot timestamp (decimal normalized). | double |
| token_amount_usd         | The amount of the token in USD.                           | double |

### General Transactions

Generic table at a user and transaction level

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| block_date               | A date representation of the timestamp (ie, YYYY-MM-DD HH:MM:SS) | date |
| chain_id                 | The standard chain id.                                    | int |
| block_number             | The ordinal block number.                                 | bigint |
| signer_address           | The transaction signer's address.                         | string |
| transaction_hash         | The unique identifier for this transaction.               | string |
| log_index                | The unique identifier for this transaction.               | bigint |
| event_name               | The string name for the event associated with log_index, corresponds to the action taken by the user (ie, deposit, withdrawal, borrow, repay, liquidation, flashloan). | string |
| transaction_fee          | The total amount of gas used in the transactions occurring in the given snapshot (in the native gas amount). | double |
| transaction_fee_usd      | (Optional, if possible) The total amount of gas used in USD terms in the given snapshot. | double |

### User Transaction Fee Snapshot

Gas and transaction snapshot data at the user level.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard chain id.                                    | int |
| user_address             | The address of the user this snapshot activity is based on. | string |
| transaction_count        | The number of transactions this user has signed in the given snapshot. | bigint |
| transaction_fees         | The total amount of gas used in the transactions occurring in the given snapshot (in the native gas amount). | double |
| transaction_fees_usd     | (Optional, if possible) The total amount of gas used in USD terms in the given snapshot. | double |

> Note: This markdown file is auto-generated.
