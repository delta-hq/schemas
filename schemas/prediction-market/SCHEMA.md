# Prediction Market

Standard table definitions for Prediction Markets.

## Version: 1.0.0-alpha

### User Positions Tracking

List of NFT transfers.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| block_timestamp          | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | number |
| user_address             | The address of the user the record is for.                | string |
| market_id                | Identifier for the market the order is placed on.         | number |
| order_id                 | Identifier for the particular limit order.                | number |
| open_order_size_usd      | The USD value of the open amount for the particular limit order. | number |
| closed_order_size_usd    | The USD value of the open amount for the particular limit order. | number |

> Note: This markdown file is auto-generated.
