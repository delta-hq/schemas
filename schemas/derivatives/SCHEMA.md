# Derivatives

OpenBlock Labs standard schema for derivatives protocols (options and perps).

## Version: 1.0.0-alpha

### Pools

Pools in the protocol (one entry for each token).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | Standard chain id.                                        | int |
| timestamp                | The timestamp of the block the pool was created on.       | timestamp |
| creation_block_number    | The block number this pool was created on.                | bigint |
| pool_address             | The contract address of the pool.                         | string |
| pool_name                | The name of the pool (ie, name() in the smart contract).  | string |
| token_index              | The index of the token in the smart contract (one row for each token in a pool). | bigint |
| token_address            | The contract address of the token.                        | string |
| token_symbol             | The symbol of the token.                                  | string |

### Pairs (AMM)

Pairs traded in the protocol (one entry for each pair).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | Standard chain id.                                        | int |
| timestamp                | The timestamp of the block the pool was created on.       | timestamp |
| creation_block_number    | The block number this pair was created on.                | bigint |
| pair_name                | The name of the pool (ie, name() in the smart contract).  | string |
| pair_index               | The index of the token in the smart contract (one row for each pair). | bigint |
| pair_address             | The contract address of the pair.                         | string |
| pair_symbol              | The symbol of the pair.                                   | string |
| vault_address            | The address of the vault where each pair are traded in.   | string |

### Pairs Snapshot (AMM)

Pairs traded in the protocol (snapshot data for each pair).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | Standard chain id.                                        | int |
| timestamp                | The timestamp of the block the pool was created on.       | timestamp |
| pair_name                | The name of the pool (ie, name() in the smart contract).  | string |
| pair_index               | The index of the token in the smart contract (one row for each pair). | bigint |
| pair_address             | The contract address of the pair.                         | string |
| pair_symbol              | The symbol of the pair.                                   | string |
| pair_liquidity           | The liquidity available for trading for the pair (at snapshot, in tokens). | double |
| pair_liquidity_usd       | The liquidity available for trading for the pair (at snapshot, in USD). | double |
| volume_usd               | The volume of each pair opened and closed in the given snapshot (at snapshot, in USD). | double |
| open_interest_longs_usd  | The sum of open interest of longs held for each pair, in USD. | double |
| open_interest_shorts_usd | The sum of open interest in shorts held for each pair, in USD. | double |
| liquidation_fees_usd     | The total liquidation fees accrued for each pair (at snapshot, in USD). | double |
| funding_rate             | The funding rate for each pair at the time of the snapshot, as a percentage. | double |
| open_fees_usd            | The total open fees accrued for each pair (at snapshot, in USD). | double |
| close_fees_usd           | The total close fees accrued for each pair (at snapshot, in USD). | double |

### LP Snapshot

Liquidity providers snapshot (one entry for each token in a pool).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | Standard chain id.                                        | int |
| pool_address             | The address of the pool.                                  | string |
| lp_address               | The address of the liquidity provider.                    | string |
| token_index              | The index of the token in the smart contract.             | bigint |
| token_address            | The address of the token provided as liquidity.           | string |
| token_symbol             | The symbol of the token.                                  | string |
| deposit_amount           | (Optional, for Order Books) The amount deposited into the pool, decimal normalized. | double |
| deposit_amount_usd       | (Optional, for Order Books) The amount deposited, in USD. | double |
| amount_useful            | (Optional, for LPs) The amount of tokens supplied that are liquid and usable by users of the protocol, decimal normalized. | double |
| amount_useful_usd        | (Optional, for LPs) The amount of liquid tokens supplied in USD. | double |
| liquidated_amount        | The amount of tokens liquidated from the LP, decimal normalized. | double |
| liquidated_amount_usd    | The amount liquidated, in USD.                            | double |
| total_fees_usd           | (Optional) All fees generated by the LP in the given snapshot in USD. | double |
| user_fees_usd            | (Optional) The portion of fees accrued to users of the protocol, in USD. | double |
| protocol_fees_usd        | (Optional) The portion of fees accrued to the protocol, in USD. | double |

### LP Snapshot (AMM)

Liquidity providers snapshot (one entry for each token in a vault).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | Standard chain id.                                        | int |
| vault_address            | The address of the vault.                                 | string |
| lp_address               | The address of the liquidity provider.                    | string |
| token_index              | The index of the token in the smart contract.             | bigint |
| token_address            | The address of the token provided as liquidity.           | string |
| token_symbol             | The symbol of the token.                                  | string |
| amount_useful            | The amount of tokens supplied by the LP that are liquid and usable by users in the vault, decimal normalized. | double |
| amount_useful_usd        | The amount of liquid tokens supplied in USD.              | double |
| liquidity_change_amount  | The amount of tokens lost (indicated by negative sign) or gained (indicated by positive sign) by the LP, decimal normalized. | double |
| liquidity_change_amount_usd | The amount lost or gained by the LP, in USD.              | double |
| total_lp_fees_usd        | Total fees generated for the LP at the time of snapshot (in USD). | double |

### Pool Snapshot

Snapshot of the pool's metrics.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | Standard chain id.                                        | int |
| pool_address             | The smart contract address of the pool.                   | string |
| token_index              | The index of the token in the smart contract (one row for each token in a pool). | bigint |
| funding_rate             | The funding rate in this pool at the time of the snapshot, as a percentage. | double |
| fee_rate                 | he pool's fee rate, as a percentage.                      | double |
| total_value_locked_usd   | The total value locked in USD.                            | double |
| volume_usd               | The volume of positions opened and closed in the given snapshot in USD. | double |
| open_interest_longs_usd  | The sum of open interest of longs held within this pool in USD. | double |
| open_interest_shorts_usd | The sum of open interest in shorts held within this pool in USD. | double |
| total_fees_usd           | The sum of fees generated by the pool in USD.             | double |

### Vault (AMM)

Vault(s) in the protocol (one entry for each vault).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the block the pool was created on.       | timestamp |
| chain_id                 | Standard chain id.                                        | int |
| vault_address            | The smart contract address of the vault.                  | string |
| token_symbol             | The symbol of the token.                                  | string |
| token_address            | The smart contract address of the token used              | string |
| token_index              | The index of the token in the smart contract.             | bigint |

### Vault Snapshot (AMM)

Snapshot of the vault's metrics.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | Standard chain id.                                        | int |
| vault_address            | The smart contract address of the vault.                  | string |
| token_address            | The smart contract address of the token.                  | string |
| token_index              | The index of the token in the smart contract.             | bigint |
| token_amount             | Total Value Locked at snapshot, in tokens.                | double |
| token_amount_usd         | Total Value Locked at snapshot (amount for each token, in USD). | double |
| liquidity_available_usd  | The total liquidity available in the vault for trading, in USD. | double |
| open_interest_longs_usd  | The aggregate value of open long positions backed by the vault’s liquidity at snapshot, in USD. | double |
| open_interest_shorts_usd | The aggregate value of open short positions backed by the vault’s liquidity at snapshot, in USD. | double |
| volume_usd               | The volume of trades generated by the vault in the given snapshot (24h rolling average, in USD). | double |
| vault_fees_usd           | The portion of fees accrued by the protocol (24h rolling average, in USD). | double |

### Trades

Trade data, 1 entry for each close, open, or update of a trade.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the trade.                               | timestamp |
| chain_id                 | Standard chain id.                                        | int |
| transaction_hash         | The hash of the transaction this trade was performed in.  | string |
| log_index                | Event log index.                                          | bigint |
| block_number             | The block number of the trade.                            | bigint |
| pool_address             | The address of the pool this token was traded in.         | string |
| maker_address            | The address of the maker.                                 | string |
| taker_address            | The address of the taker.                                 | string |
| token_address            | The address of the token.                                 | string |
| amount                   | The value that a trader is putting to open a long or short, decimal normalized. | double |
| amount_usd               | The trade amount in USD.                                  | double |
| notional_value           | The value of the leveraged amount of the trade, decimal normalized. | double |
| notional_value_usd       | The notional value, in USD.                               | double |
| maker_pnl_usd            | (Only applicable on trade close) The total profit and loss of the trade on the maker's side, in USD. | double |
| taker_pnl_usd            | (Only applicable on trade close) The total profit and loss of the trade on the taker's side, in USD. | double |
| trade_action             | The action of trade being recorded in this entry (ie, OPEN, CLOSE, INCREASE, DECREASE, LIQUIDATED). | string |
| trade_type               | The type of the trade being recorded in this entry (ie, LONG, SHORT). | string |

### Trades (AMM)

Trade data, one entry for each close, open, or update of a trade.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the trade.                               | timestamp |
| chain_id                 | Standard chain id.                                        | int |
| transaction_hash         | The hash of the transaction this trade was performed in.  | string |
| log_index                | Event log index.                                          | bigint |
| block_number             | The block number of the trade.                            | bigint |
| pool_address             | The address of the pool this token was traded in.         | string |
| taker_address            | The address of the taker.                                 | string |
| pair_index               | The address of the pair that is traded.                   | bigint |
| amount                   | The value that a trader is putting (and used as collateral) to open a long or a short, decimal normalized. | double |
| amount_usd               | The trade amount in USD (if deposit is only made in stable, amount = amount_usd). | double |
| notional_value           | The value of the leveraged amount of the trade, decimal normalized. | double |
| notional_value_usd       | The notional value, in USD.                               | double |
| open_interest_longs_usd  | The aggregate value of open long positions held by the trader at snapshot, in USD. | double |
| open_interest_shorts_usd | The aggregate value of open short positions held by the trader at snapshot, in USD. | double |
| taker_pnl_usd            | (Only applicable after trade is closed) The total profit and loss of the trade on the taker's side, in USD. | double |
| trade_action             | The action of trade being recorded in this entry (ie, OPEN, CLOSE, INCREASE, DECREASE, LIQUIDATED). | string |
| trade_type               | The type of the trade being recorded in this entry (ie, LONG, SHORT). | string |
| open_fee_rate            | The open fee applied to to the taker trade, as percentage. | double |
| close_fee_rate           | The close fee applied to to the taker trade, as percentage. | double |
| open_fee_usd             | The open fee applied to to the taker trade, in USD.       | double |
| close_fee_usd            | The close fee applied to to the taker trade, in USD.      | double |
| liquidation_fee_rate     | (If applicable, i.e. PnL<0, 0 otherwise) The liquidation fee applied to to the taker trade, as percentage. | double |
| liquidation_fee_usd      | (If applicable, i.e. PnL<0, 0 otherwise) The liquidation fee applied to to the taker trade, in USD. | double |

### Liquidity Transaction Events

Event data capturing activities related to liquidity transactions, including deposits and withdrawals

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the trade.                            | number |
| log_index                | The event log. For transactions that don't emit events, create an arbitrary index starting from 0. | number |
| transaction_hash         | The hash of the transaction.                              | string |
| user_address             | The address that initiates the transaction (i.e., the transaction signer). | string |
| taker_address            | The address that receives the output of the event (i.e., the account that receives LP receipt tokens). | string |
| pool_address             | The contract address of the pool.                         | string |
| token_address            | The address of the underlying token that was interacted with. | string |
| token_index              | The index of the token in the smart contract (one row for each token in a pool). | string |
| token_amount             | The amount of token_address transacted, decimal normalized. | number |
| token_amount_usd         | The amount of token_address transacted, in USD.           | number |
| event_type               | The type of event, corresponds to the action taken by the user (e.g., deposit, withdrawal). | string |

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
| other_incentive_usd      | (Optional) Any incentives outside of the claimed token, in this transaction, summed up in USD terms. | double |

> Note: This markdown file is auto-generated.
