/*-
 * Copyright (c) <2010-2020>, Intel Corporation. All rights reserved.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */
/* Created 2021 by Diego Rossi Mafioletti @ gmail.com */

#ifndef _PKTGEN_VOLT_H_
#define _PKTGEN_VOLT_H_

#include "pktgen-seq.h"

#ifdef __cplusplus
extern "C" {
#endif

struct rte_volt_us_ether_hdr {
    uint64_t out_dstAddr:48;
    uint64_t out_srcAddr:48;
    uint16_t out_chunck_len;
    uint16_t burst_id;
    uint8_t burst_seq;
    uint8_t flags;
    uint32_t padding;
    uint64_t ploamu[6];
} __rte_packed;

struct rte_volt_dbru_hdr {
    uint32_t buff_occ:24;
    uint8_t crc;    
} __rte_packed;

#ifdef __cplusplus
}
#endif

// pktgen_volt_ctor(pkt_seq_t *pkt, void *hdr);

// pktgen_packet_insert_dbru(port_info_t *info, uint16_t qid);


#endif  /*  _PKTGEN_VOLT_H_ */
