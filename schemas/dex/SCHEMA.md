# DEX

Standard table definitions for dex protocols.

## Version: 1.0.0

### Pools

List of LP pools in this protocol (one entry per token in a pool).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | The standard id of the chain.                             | int |
| creation_block_number    | The block this pool was created in.                       | bigint |
| timestamp                | The timestamp of the block that this pool was created in. | timestamp |
| pool_address             | The contract address of the LP pool.                      | string |
| lp_token_address         | The token address of the LP token for this pool.          | string |
| lp_token_symbol          | The symbol of the LP token.                               | string |
| token_address            | The token address of the pool token at token_index.       | string |
| token_symbol             | The symbol of the pool token.                             | string |
| token_decimals           | The decimals of the pool token.                           | string |
| token_index              | The index in the pool smart contract that this token appears at, default 0 (ie, one entry per token in a pool). | bigint |
| fee_rate                 | (Optional, if dynamic fee) The fee rate of the pool, as a percentage (ie, 2.3% as 0.023). | double |
| dex_type                 | The type of the DEX (ie, CPMM, CLMM, Orderbook).          | string |

### LP Position Snapshot

Snapshot of LP positions.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | int |
| pool_address             | The contract address of the pool.                         | string |
| user_address             | The address of the liquidity provider.                    | string |
| token_index              | The token index based on the smart contract.              | bigint |
| token_address            | The contract address of the token provided as liquidity.  | string |
| token_symbol             | The symbol of the token.                                  | string |
| token_amount             | The amount of the underlying liquidity position in the pool, decimal normalized (ie, the amount of USDC provided by the LPer in a USDC/WETH pool). | double |
| token_amount_usd         | The amount of the token in USD.                           | double |

### Pool Snapshot

Snapshot of pool states.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | int |
| pool_address             | The contract address of the LP pool.                      | string |
| token_index              | The token index in the smart contract.                    | bigint |
| token_address            | The contract address of the token in the pool.            | string |
| token_symbol             | The symbol of the token.                                  | string |
| token_amount             | The amount of the token in this pool at the snapshot.     | double |
| token_amount_usd         | The amount of the token in USD.                           | double |
| volume_amount            | The volume of the token transacted in this pool during the given snapshot, decimal normalized. | double |
| volume_usd               | The volume transacted in the given snapshot, in USD.      | double |
| fee_rate                 | The fee rate of the pool, as a percentage (ie, 2.3% as 0.023). | double |
| total_fees_usd           | The total amount of revenue and fees paid in this pool in the given snapshot, in USD. | double |
| user_fees_usd            | The amount of total fees accrued to liquidity providers of the protocol, in USD. | double |
| protocol_fees_usd        | The amount of total fees accrued to the protocol, in USD. | double |

### Trades (All DEX Types)

All trades across different types of DEXs.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the trade.                            | bigint |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| user_address             | The address that initiates the transaction (ie, the transaction signer). | string |
| taker_address            | The taker, the address that receives the output of the swap (ie, could be the same as user_address unless a proxy contract/router is used). | string |
| maker_address            | The maker, the address that receives the input of the swap (ie, could be the same as user_address unless a proxy contract/router is used). | string |
| pair_name                | The name of the token pair.                               | string |
| pool_address             | The contract address of the LP pool being traded in.      | string |
| input_token_address      | The contract address of the input token (ie, the tokenIn or the token being sold to the pool). | string |
| input_token_symbol       | The symbol of the input token.                            | string |
| input_token_amount       | The amount of the input token, decimal normalized.        | double |
| output_token_address     | The contract address of the output token (ie, the tokenOut of the token being bought by the user and sent to the taker). | string |
| output_token_symbol      | The symbol of the output token.                           | string |
| output_token_amount      | The amount of the output token, decimal normalized.       | double |
| spot_price_after_swap    | The spot price in the pool after the swap is complete. This is the price ratio a user would get if they made an infinitesimal swap immediately after this one. | double |
| swap_amount_usd          | The amount of the swap in USD.                            | double |
| fees_usd                 | The fees paid by the user.                                | double |

### User Score Snapshot

Snapshot of user scores.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the record.                              | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the record.                           | bigint |
| user_address             | The address of the user.                                  | string |
| pool_address             | The contract address of the pool.                         | string |
| market_depth_score       | (Ask for supporting documents and formula). The percentage price range market depth derived from a 30-day realized volatility. | double |
| total_value_locked_score | A score calculated based on TVL. Please see the methodology [here](./METHODOLOGY.md). | double |

### V2 Mints

Mint events for V2.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the record.                              | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the mint.                             | bigint |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| transaction_from_address | The address that initiates the transaction (ie, the transaction signer). | string |
| from_address             | The from address of the event (ie, the from field in a transfer). | string |
| to_address               | The to address of the event (ie, the to field in a transfer). | string |
| pool_address             | The contract address of the pool.                         | string |
| token0_address           | The contract address of token0.                           | string |
| token0_amount            | The amount of token0.                                     | double |
| token1_address           | The contract address of token1.                           | string |
| token1_amount            | The amount of token1.                                     | double |
| mint_amount              | The amount of LP token minted by the trader, decimal normalized. | double |
| mint_amount_usd          | The amount of the mint in USD.                            | double |

### V2 Burns

Burn events for V2.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the trade.                            | bigint |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| transaction_from_address | The address that initiates the transaction (ie, the transaction signer). | string |
| from_address             | The from address of the event (ie, the from field in a transfer). | string |
| to_address               | The to address of the event (ie, the to field in a transfer). | string |
| pool_address             | The contract address of the pool.                         | string |
| token0_address           | The contract address of token0.                           | string |
| token0_amount            | The amount of token0.                                     | double |
| token1_address           | The contract address of token1.                           | string |
| token1_amount            | The amount of token1.                                     | double |
| burn_amount              | The amount of LP tokens burned, decimal normalized.       | double |
| burn_amount_usd          | The amount of the burn in USD.                            | double |

### V2 Syncs

Sync events for V2.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the trade.                            | bigint |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| pool_address             | The contract address of the pool.                         | string |
| token0_address           | The contract address of token0.                           | string |
| token0_amount            | The amount of token0.                                     | double |
| token1_address           | The contract address of token1.                           | string |
| token1_amount            | The amount of token1.                                     | double |

### V2 Transfers

Transfer events for V2.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the trade.                            | bigint |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| transaction_from_address | The address that initiates the transaction (ie, the transaction signer). | string |
| from_address             | The address that sends the LP token.                      | string |
| to_address               | The address that receives the LP token.                   | string |
| pool_address             | The contract address of the pool.                         | string |
| token_amount             | The token amount that was transferred, decimal normalized. | double |

### V3 Events

LP burn/mint events for V3 DEXs.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the trade.                            | bigint |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| transaction_from_address | The address that initiates the transaction (ie, the transaction signer). | string |
| event_type               | The action type of the event (ie, mint, burn).            | string |
| pool_address             | The contract address of the pool.                         | string |
| tick_lower               | The lower tick of the liquidity position.                 | double |
| tick_upper               | The upper tick of the liquidity position.                 | double |
| current_tick             | The current tick of the liquidity pool.                   | double |
| tick_spacing             | The tick spacing of the liquidity pool.                   | double |
| nft_token_id             | The token ID of the NFT that represents the liquidity position | string |
| token0_address           | The contract address of token0.                           | string |
| token0_amount            | The amount of token0(raw token amount).                   | double |
| token1_address           | The contract address of token1.                           | string |
| token1_amount            | The amount of token1(raw token amount).                   | double |
| token_fees               | The amount of token fees.                                 | double |
| amount_liquidity         | The amount of liquidity.                                  | double |

### V3 Transfers

LP transfer events for V3 DEXs.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the trade.                            | bigint |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| transaction_from_address | The address that initiates the transaction (ie, the transaction signer). | string |
| from_address             | The from address of the event (ie, the from field in a transfer). | string |
| to_address               | The to address of the event (ie, the to field in a transfer). | string |
| nft_token_id             | The token ID of the NFT transferred                       | string |
| event_type               | The action type of the event (ie, transfer).              | string |

### Liquidity Transaction Events (General)

Event data capturing activities related to liquidity transactions, including deposits and withdrawals

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | timestamp |
| chain_id                 | The standard id of the chain.                             | int |
| block_number             | The block number of the transaction.                      | bigint |
| log_index                | The event log. For transactions that don't emit events, create arbitrary index starting from 0. | bigint |
| transaction_hash         | The hash of the transaction.                              | string |
| user_address             | The address that initiates the transaction (i.e., the transaction signer). | string |
| taker_address            | The address that receives the output of the event (i.e., the account that receives LP receipt tokens). | string |
| pool_address             | The contract address of the pool.                         | string |
| token_address            | The address of the underlying token that was interacted with. | bigint |
| token_index              | The index in the pool smart contract that this token appears at, default 0 (ie, one entry per token in a pool). | bigint |
| token_amount             | The token amount of the underlying asset being added/removed from the pool , decimal normalized | double |
| token_amount_usd         | The amount of the token in USD.                           | double |
| event_type               | The type of event, corresponds to the action taken by the user (e.g., deposit, withdrawal). | double |

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
