# Launchpad

Standard table definitions for Launchpads.

## Version: 1.0.0-alpha

### Bonding Curve Snapshot

Snapshots of the bonding curve for pre-graduation tokens, with token amounts and their USD values.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard chain id.                                    | number |
| pool_address             | Contract address of the bonding curve, or an identifier that is unique for this bonding curve. | string |
| token_index              | The token index based on the smart contract.              | number |
| token_address            | The smart contract address of the token.                  | string |
| token_symbol             | The symbol of the token we are getting the balance of.    | string |
| token_amount             | The amount of the token at the given snapshot timestamp (decimal normalized). | number |
| token_amount_usd         | The amount of the token in USD.                           | number |

### Token Balance Snapshot

Snapshots of each user address' token balance of the launchpad tokens.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard chain id.                                    | number |
| user_address             | The address of the user this snapshot activity is based on. | string |
| token_address            | The smart contract address of the token.                  | string |
| token_symbol             | The symbol of the token we are getting the balance of.    | string |
| token_amount             | The amount of the token at the given snapshot timestamp (decimal normalized). | number |
| token_amount_usd         | The amount of the token in USD.                           | number |

### LP Position Snapshot

Snapshots of liquidity in the burnt LP position of graduated tokens.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | number |
| pool_address             | The contract address of the pool.                         | string |
| user_address             | The address of the liquidity provider.                    | string |
| token_index              | The token index based on the smart contract.              | number |
| token_address            | The contract address of the token provided as liquidity.  | string |
| token_symbol             | The symbol of the token provided as liquidity.            | string |
| token_amount             | The amount of the underlying liquidity position in the pool, decimal normalized (ie, the amount of USDC provided by the LPer in a USDC/WETH pool). | number |
| token_amount_usd         | The amount of the token in USD.                           | number |

> Note: This markdown file is auto-generated.
