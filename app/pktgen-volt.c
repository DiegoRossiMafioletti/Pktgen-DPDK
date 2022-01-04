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
pktgen_volt_ctor(pkt_seq_t *pkt, void *hdr)
{
	struct  *volt = hdr;
	uint16_t tlen;
}

void
pktgen_packet_insert_dbru(port_info_t *info, uint16_t qid) 
{
	pkt_seq_t *pkt = &info->seq_pkt[seq_idx];
	struct rte_volt_us_ether_hdr *volt_us = (struct rte_volt_us_ether_hdr *)&pkt->hdr.eth;// or .volt_us: find who is this "pkt"
	struct rte_volt_dbru_hdr *dbru;
	uint32_t flags;

	flags = rte_atomic32_read(&info->port_flags);
	char *l3_hdr = (char *)&volt_us[1];	/* Point to l3 hdr location */


	volt_us

}