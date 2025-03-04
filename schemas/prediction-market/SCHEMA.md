# Prediction Market

Standard table definitions for Prediction Markets.

## Version: 1.0.0-alpha

### User Positions Snapshot

Prediction market order snapshots.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot (in unix time).             | timestamp |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | int |
| user_address             | The address of the user that owns this order in the snapshot. | string |
| market_address           | The smart contract of the address of the market (if no smart contract, please create a unique identifier for the market). | string |
| order_id                 | Identifier for the particular limit order.                | bigint |
| open_order_size_usd      | The USD value of the open amount for this particular limit order. | double |
| closed_order_size_usd    | The USD value of the open amount for this particular limit order in the interval for the given timestamp. | double |
| locked_order_size_usd    | The USD value of the open filled and matched for this particular limit order. | double |
| poll_open_timestamp      | The timestamp that the poll opens at.                     | timestamp |
| poll_close_timestamp     | The timestamp that the poll closes at.                    | timestamp |

> Note: This markdown file is auto-generated.
