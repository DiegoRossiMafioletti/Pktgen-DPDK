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
#include "pktgen-volt.h"

/**************************************************************************//**
 *
 * pktgen_volt_ctor - Construct the VOLT header for a packet
 *
 * DESCRIPTION
 * Constructor for the XGEM header for a given packet.
 *
 * RETURNS: N/A
 *
 * SEE ALSO:
 */

void
pktgen_volt_hdr_ctor(pkt_seq_t *pkt __rte_unused, void *hdr)
{
	struct rte_volt_us_ether_hdr *volt = hdr;
	uint8_t i;

	// volt->out_chunck_len = htons(pkt->ethType);
	volt->burst_id = 0;
	volt->burst_seq = 1;
	volt->flags = 0x02;
	volt->padding = 0x00000000;
	for (i = 0; i < 48; i++) {
		volt->ploamu[i] = 0x44;
	}
}