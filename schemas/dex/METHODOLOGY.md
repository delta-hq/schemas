# Methodology Specification for TVL Score Calculation

## Overview

**DEX Protocols** are required to provide a **Total Value Locked (TVL) Score** under the table `user_score_snapshot`. This score represents the TVL of individual addresses on a given pool and timestamp. To protect against manipulation, filters should be applied to LP positions to ensure they are providing utility on the DEX. These filters for common DEX designs are described below.

## TVL Filters

The filters and transformations to be applied to TVL for common DEX designs are outlined below.

### Constant Product Market Maker (CPMM) + Stableswap

For CPMM designs, as all LP positions are utilized regardless of the current pool price, **no filter** is needed. The TVL value returned should be the **USD value of the LP position** on the pool.

### Concentrated Liquidity Market Maker (CLMM)

To ensure that LP liquidity provided is usable for swappers, the TVL value returned should be the **USD value of all LP positions that are in range** of the active tick. Specifically, for the given pool, this is the **USD value of all LP positions** where the active tick is:

- Greater than or equal to the position’s lower tick, and
- Less than or equal to the position’s upper tick.

### Central Limit Order Book (CLOB)

To ensure that all limit orders are reasonably close to the current price of a token pair, and thus providing useful liquidity, the TVL value returned should be the **USD value of a user’s limit orders within +/- X% of the current midpoint price**.

- The value of **X** varies by pool to reflect expected price ranges for stable and volatile token pairs.
- **X** should be calculated as the **95th percentile of absolute hourly returns** over a rolling 7-day period.
- By taking the absolute value of hourly changes in price for the pool over the past 7 days, 95% of values should be less than or equal to **X**.

### Other AMM Designs

For novel AMM designs, please contact **OpenBlock Labs** via the established Telegram channel to discuss how to appropriately evaluate the useful liquidity on your protocol.

## Questions

If any other questions arise, please contact **OpenBlock Labs** via the established Telegram channel to discuss further.
