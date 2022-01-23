/*-
 * Copyright (c) <2010-2020>, Intel Corporation. All rights reserved.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

/* Created 2010 by Keith Wiles @ intel.com */

#include <arpa/inet.h>

#include <cli_scrn.h>
#include <lua_config.h>

#include "pktgen.h"
#include "pktgen-log.h"
#include "pktgen-pon.h"

/**************************************************************************//**
 *
 * pktgen_pon_ctor - Construct the PON header for a packet
 *
 * DESCRIPTION
 * Constructor for the XGEM header for a given packet.
 *
 * RETURNS: N/A
 *
 * SEE ALSO:
 */

void
pktgen_pon_hdr_ctor(pkt_seq_t *pkt __rte_unused, void *hdr)
{
	struct rte_pon_us_ether_hdr *pon = hdr;
	uint8_t i;

	pon->burst_id = 0;
	pon->burst_seq = 1;
	pon->flags = 0x02;
	pon->padding = 0x00000000;
	for (i = 0; i < 48; i++) {
		pon->ploamu[i] = 0x44;
	}
}