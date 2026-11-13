# OpenJanela for Windows & Doors

An OpenJanela entry in your Odoo apps menu, so your team reaches your OpenJanela
server (hosted or self-hosted) in one click — and everything the integration
needs to get started.

OpenJanela is the quoting, drawing and production engine for window and door
makers:

- **Product configurator** with rules-based pricing — price every option
  without a programmer
- **Shop drawings** generated from the configuration
- **Bills of material, cut lists and optimization** (glass, aluminum, vinyl)
- **Label printing and shop-floor tracking** — batches, stations, barcode scans,
  QC and packing
- Works **with Odoo 19**: quote configured windows and doors from the Odoo
  sales order; prices, drawings and BOMs come back into Odoo

## What this module is (and is not)

This module is a **launcher**: it adds the OpenJanela app menu and one setting
(the URL of your OpenJanela server). It adds no tables, no fields on your
records and no business logic — safe to install on any Odoo 19 database.

The full integration is a thin API connection set up from the OpenJanela side
(Odoo 19 JSON-2 API, no module needed inside Odoo): customers, quotations,
orders, drawings, production dates and stock levels stay in sync. Start at
**Connect OpenJanela to Odoo** in the OpenJanela menu, or
<https://openjanelaerp.com/openjanela-for-odoo>.

## Configuration

1. Install the module.
2. Go to *Settings → General Settings → OpenJanela* and set the **OpenJanela
   URL** (your hosted address, or your own server if you self-host).
3. Click the OpenJanela app — it opens in a new tab.

## Licence

LGPL-3. The module is free. OpenJanela itself is free to self-host (source
download) with paid modules and hosting available.

## Links

- Product: <https://openjanelaerp.com/openjanela-for-odoo>
- Source: <https://github.com/openjanela/openjanela>
