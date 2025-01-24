# Lending / MM / CDP

Standard table definitions for lending protocols.

## Version: 1.0.0

### Pools

List of pools in the lending protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | The standard id of the chain.                             | int |
| creation_block_number    | The block this pool was created in.                       | bigint |
| timestamp                | The timestamp of the block that this pool was created in. | timestamp |
| underlying_token_address | The contract address of the underlying token.             | string |
| underlying_token_symbol  | The symbol of the underlying token.                       | string |
| receipt_token_address    | The contract address of the receipt token.                | string |
| receipt_token_symbol     | The symbol of the receipt token.                          | string |
| pool_address             | The contract address of the pool.                         | string |
| market_address           | The contract responsible for configuring the market parameters (e.g., Comptroller in Compound or Pool Configurator in Aave) | string |
| pool_type                | The type of the pool (collateral_only, isolated, supply_pool, cdp). | string |

### Position Snapshot

Snapshot of user positions in the lending protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | int |
| pool_address             | The contract address of the pool.                         | string |
| underlying_token_address | The contract address of the underlying token.             | string |
| underlying_token_symbol  | The symbol of the underlying token.                       | string |
| user_address             | The address of the user who has the position.             | string |
| supplied_amount          | The amount supplied by the user in the underlying token, decimal normalized. | double |
| supplied_amount_usd      | The supplied amount in USD.                               | double |
| borrowed_amount          | The amount borrowed by the user in the underlying token, decimal normalized. | double |
| borrowed_amount_usd      | The borrowed amount in USD.                               | double |
| collateral_amount        | The amount of collateral-only tokens of this asset, decimal normalized. | double |
| collateral_amount_usd    | The amount of collateral-only tokens in USD.              | double |

### Pool Snapshot

Snapshot of the pool's state in the lending protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | int |
| pool_address             | The contract address of the pool.                         | string |
| underlying_token_address | The contract address of the underlying token.             | string |
| underlying_token_symbol  | The symbol of the underlying token.                       | string |
| underlying_token_price_usd | The token price of the underlying asset in USD.           | double |
| available_amount         | The amount of token's available to borrow (liquidity or net supply or supply - borrow). | double |
| available_amount_usd     | The available amount of token's in this pool in USD.      | double |
| supplied_amount          | The total amount of the underlying token supplied in this pool, decimal normalized. | double |
| supplied_amount_usd      | The supplied amount in USD.                               | double |
| collateral_amount        | The amount of collateral only tokens in this pool.        | double |
| collateral_amount_usd    | The amount of collateral only tokens in the pool.         | double |
| collateral_factor        | The collateral factor of the pool (defined as a decimal percentage, between 0-100). | double |
| supply_index             | The supply index of the pool.                             | double |
| supply_apr               | The current annual percentage rate for supplied amount, as a decimal percentage. | double |
| borrowed_amount          | The amount of underlying tokens borrowed from this pool in the underlying token, decimal normalized. | double |
| borrowed_amount_usd      | The borrowed amount in USD.                               | double |
| borrow_index             | The borrow index of the pool.                             | double |
| borrow_apr               | The current annual percentage rate for borrow, as a decimal percentage. | double |
| total_fees_usd           | The total revenue or fees accrued in this pool during the given snapshot period (ie, user_fees_usd + protocol_fees_usd = total_fees_usd). | double |
| user_fees_usd            | The portion of total revenue or fees accrued to users of the protocol during the given snapshot period. | double |
| protocol_fees_usd        | The portion of total revenue or fees accrued to protocol during the given snapshot period. | double |

### Events

All user events in the lending protocol (ie, Deposit, Withdrawal, Borrow, Repay, Flashloan)

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the trade.                            | bigint |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| user_address             | The address that initiates the transaction (ie, the transaction signer). | string |
| taker_address            | The address that receives the output of the event (ie, account that receives aTokens in an Aave Deposit). | string |
| pool_address             | The contract address of the pool.                         | string |
| token_address            | The address of the underlying token that was interacted with (ie, USDC and not aUSDC in Aave). | string |
| amount                   | The amount of token_address transacted, decimal normalized. | double |
| amount_usd               | The amount of token_address transacted, in USD.           | double |
| event_type               | The type of lending event, corresponds to the action taken by the user (ie, deposit, withdrawal, borrow, repay, liquidation, flashloan). | string |

### Liquidations

Liquidation events, including profit and liquidator.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the trade.                            | bigint |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| liquidator_address       | The address that initiates the liquidation.               | string |
| user_address             | The address that was liquidated.                          | string |
| pool_address             | The contract address of the pool.                         | string |
| token_address            | The address of the underlying token that was repaid by the liquidator (ie, USDC and not aUSDC in Aave). | string |
| amount                   | The amount of token_address transacted, decimal normalized. | double |
| amount_usd               | The amount of token_address transacted, in USD.           | double |
| profit_usd               | The amount of profit the liquidator made from liquidating user_address (can be negative). | double |

### Incentive Claim Data

Transactional data on user level incentives claimed data.

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
| other_incentive_usd      | Any incentives outside of the claimed token, in this transaction, summed up in USD terms. | double |

> Note: This markdown file is auto-generated.
