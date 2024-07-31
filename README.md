[![OBL](./docs/images/obl-logo.jpeg)](https://www.openblocklabs.com/)
# OpenBlock Labs Schemas

Welcome to OpenBlock Lab's canonical schema repository!

## About

This repository will house the source of truth for our externally facing standard schema. You can think of this is a base layer schema for any protocol to follow. In turn, this integrates into our products seamlessly.

- There is a schema, tables / entities for each protocol vertical.
- Each protocol vertical schema has a version following [semver](https://semver.org/).
- Schemas can be programatically accessed in this repository.
- These schemas can support non-breaking additions to any base schema. This may be required for some analytics.

## Schemas

Below you will find links to each of the following verticals.

- General
- DEX (Decentralized Exchange)
- Lending / CDP (Collateralized Debt Position)
- Perpetuals / Options / Derivatives
- Pool-Based Bridge
- Mint-Based Bridge
- Intent-Based Bridge
- LSTs (Liquid Staking Tokens)
- [Yield Aggregators](./schemas/yield-aggregator/SCHEMA.md) (Leverage, Gambling, RWA, ALM, Liquidity/LP, Index)
- [DEX Aggregator](./schemas/dex-aggregator/SCHEMA.md)
- Restaking
- AVS
- LRT (Liquid Restaking Tokens)
- [NFT](./schemas/nft/SCHEMA.md)
