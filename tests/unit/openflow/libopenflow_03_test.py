#!/usr/bin/env python

import unittest
import sys
import os.path
import struct
from copy import copy
sys.path.append(os.path.dirname(__file__) + "/../../..")

from pox.openflow_12.libopenflow_03 import *
from pox.datapaths.switch_03 import *

from pox.lib.packet import *

def extract_num(buf, start, length):
  """ extracts a number from a raw byte string. Assumes network byteorder  """
  # note: purposefully does /not/ use struct.unpack, because that is used by the code we validate 
  val = 0
  for i in range(start, start+length):
    val <<= 8
    val += ord(buf[i])
  return val

class ofp_message_test(unittest.TestCase):
  # test each message to see if it behaves how it should
  # each of these should be its own class so check sizes of things
  # maybe do pack/unpack here?
  
  def build_header(self, header_type):
    return ofp_header(header_type)
    
  
  def test_ofp_switch_features(self):
    # spec defines as so:
    # struct ofp_header header
    # unit64_t datapath_id
    # unit32_t n_buffers
    # uint8_t n_tables
    # uint8_t pad[3]
    # uint32_t capabilities
    # uint32_t reserved
    # struct ofp_port ports[0]
    #header = self.build_header(ofp_type["OFPT_FEATURES_REPLY"])
    # make some random number of ports
    #ports
  
  def test_ofp_switch_features(self):
    
    

class ofp_const_test(unittest.TestCase):
  # get this test to check all constants
  # at the moment we don't find constants that shouldn't be set
  # e.g. we need a test to fail when it finds OFPAT_SET_VLAN_VID that is
  # valid in OF1.1 but not in OF1.2
  
  def runtests(self, testpairs, testobj):
    self.assertTrue(testobj in globals(), "Map %s isn't defined" % testobj)
    testmap = globals()["%s_map" % testobj]
    for const, expected in testpairs.iteritems():
      self.assertTrue(expected in testmap, "Const %s not in %s" % (const, testobj))
      self.assertEquals(testmap[expected], const, "Const %s should be %s, but %s is" % (const, expected, testmap[expected]))
    
  
  def test_ofp_type(self):
    testpairs = {
      "OFPT_HELLO" : 0,
      "OFPT_ERROR" : 1,
      "OFPT_ECHO_REQUEST" : 2,
      "OFPT_ECHO_REPLY" : 3,
      "OFPT_EXPERIMENTER" : 4,
      "OFPT_FEATURES_REQUEST" : 5,
      "OFPT_FEATURES_REPLY" : 6,
      "OFPT_GET_CONFIG_REQUEST" : 7,
      "OFPT_GET_CONFIG_REPLY" : 8,
      "OFPT_SET_CONFIG" : 9,
      "OFPT_PACKET_IN" : 10,
      "OFPT_FLOW_REMOVED" : 11,
      "OFPT_PORT_STATUS" : 12,
      "OFPT_PACKET_OUT" : 13,
      "OFPT_FLOW_MOD" : 14,
      "OFPT_GROUP_MOD" : 15,
      "OFPT_PORT_MOD" : 16,
      "OFPT_TABLE_MOD" : 17,
      "OFPT_STATS_REQUEST" : 18,
      "OFPT_STATS_REPLY" : 19,
      "OFPT_BARRIER_REQUEST" : 20,
      "OFPT_BARRIER_REPLY" : 21,
      "OFPT_QUEUE_GET_CONFIG_REQUEST" : 22,
      "OFPT_QUEUE_GET_CONFIG_REPLY" : 23,
      "OFPT_ROLE_REQUEST" : 24,
      "OFPT_ROLE_REPLY" : 25,
    }
    testobj = "ofp_type"
    self.runtests(testpairs, testobj)
  
  def test_ofp_port_config(self):
    testpairs = {
      "OFPPC_PORT_DOWN" : 1 << 0,
      "OFPPC_NO_RECV" : 1 << 2,
      "OFPPC_NO_FWD" : 1 << 5,
      "OFPPC_NO_PACKET_IN" : 1 << 6,
    }
    testobj = "ofp_port_config"
    self.runtests(testpairs, testobj)
  
  def test_ofp_port_state(self):
    testpairs = {
      "OFPPS_LINK_DOWN" : 1 << 0,
      "OFPPS_BLOCKED" : 1 << 1,
      "OFPPS_LIVE" : 1 << 2,
    }
    testobj = "ofp_port_state"
    self.runtests(testpairs, testobj)
  
  def test_ofp_port_no(self):
    testpairs = {
      "OFPP_MAX" : 0xffffff00,
      "OFPP_IN_PORT" : 0xfffffff8,
      "OFPP_TABLE" : 0xfffffff9,
      "OFPP_NORMAL" : 0xfffffffa,
      "OFPP_FLOOD" : 0xfffffffb,
      "OFPP_ALL" : 0xfffffffc,
      "OFPP_CONTROLLER" : 0xfffffffd,
      "OFPP_LOCAL" : 0xfffffffe,
      "OFPP_ANY" : 0xffffffff,
    }
    testobj = "ofp_port_no"
    self.runtests(testpairs, testobj)
  
  def test_ofp_port_features(self):
    testpairs = {
      "OFPPF_10MB_HD" : 1 << 0,
      "OFPPF_10MB_FD" : 1 << 1,
      "OFPPF_100MB_HD" : 1 << 2,
      "OFPPF_100MB_FD" : 1 << 3,
      "OFPPF_1GB_HD" : 1 << 4,
      "OFPPF_1GB_FD" : 1 << 5,
      "OFPPF_10GB_FD" : 1 << 6,
      "OFPPF_40GB_FD" : 1 << 7,
      "OFPPF_100GB_FD" : 1 << 8,
      "OFPPF_1TB_FD" : 1 << 9,
      "OFPPF_OTHER" : 1 << 10,
      "OFPPF_COPPER" : 1 << 11,
      "OFPPF_FIBER" : 1 << 12,
      "OFPPF_AUTONEG" : 1 << 13,
      "OFPPF_PAUSE" : 1 << 14,
      "OFPPF_PAUSE_ASYM" : 1 << 15,
    }
    testobj = "ofp_port_features"
    self.runtests(testpairs, testobj)
  
  def test_ofp_queue_properties(self):
    testpairs = {
      "OFPQT_MIN_RATE" : 1,
      "OFPQT_MAX_RATE" : 2,
      "OFPQT_EXPERIMENTER" : 0xffff,
    }
    testobj = "ofp_queue_properties"
    self.runtests(testpairs, testobj)
  
  def test_ofp_match_type(self):
    testpairs = {
      "OFPMT_STANDARD" : 0,
      "OFPMT_OXM" : 1,
    }
    testobj = "ofp_match_type"
    self.runtests(testpairs, testobj)
  
  def test_ofp_oxm_class(self):
    testpairs = {
      "OFPXMC_NXM_0" : 0x0000,
      "OFPXMC_NXM_1" : 0x0001,
      "OFPXMC_NXM_OPENFLOW_BASIC" : 0x8000,
      "OFPXMC_NXM_EXPERIMENTER" : 0xFFFF,
    }
    testobj = "ofp_oxm_class"
    self.runtests(testpairs, testobj)
  
  def test_ofp_oxm_class(self):
    testpairs = {
      "OFPXMC_NXM_0" : 0x0000,
      "OFPXMC_NXM_1" : 0x0001,
      "OFPXMC_NXM_OPENFLOW_BASIC" : 0x8000,
      "OFPXMC_NXM_EXPERIMENTER" : 0xFFFF,
    }
    testobj = "ofp_oxm_class"
    self.runtests(testpairs, testobj)
  
  def test_ofp_oxm_ofb_match_field(self):
    testpairs = {
      "OFPXMT_OFB_IN_PORT" : 0,
      "OFPXMT_OFB_IN_PHY_PORT" : 1,
      "OFPXMT_OFB_METADATA" : 2,
      "OFPXMT_OFB_ETH_DST" : 3,
      "OFPXMT_OFB_ETH_SRC" : 4,
      "OFPXMT_OFB_ETH_TYPE" : 5,
      "OFPXMT_OFB_VLAN_VID" : 6,
      "OFPXMT_OFB_VLAN_PCP" : 7,
      "OFPXMT_OFB_IP_DSCP" : 8,
      "OFPXMT_OFB_IP_ECN" : 9,
      "OFPXMT_OFB_IP_PROTO" : 10,
      "OFPXMT_OFB_IPV4_SRC" : 11,
      "OFPXMT_OFB_IPV4_DST" : 12,
      "OFPXMT_OFB_TCP_SRC" : 13,
      "OFPXMT_OFB_TCP_DST" : 14,
      "OFPXMT_OFB_UDP_SRC" : 15,
      "OFPXMT_OFB_UDP_DST" : 16,
      "OFPXMT_OFB_SCTP_SRC" : 17,
      "OFPXMT_OFB_SCTP_DST" : 18,
      "OFPXMT_OFB_ICMPV4_TYPE" : 19,
      "OFPXMT_OFB_ICMPV4_CODE" : 20,
      "OFPXMT_OFB_ARP_OP" : 21,
      "OFPXMT_OFB_ARP_SPA" : 22,
      "OFPXMT_OFB_ARP_TPA" : 23,
      "OFPXMT_OFB_ARP_SHA" : 24,
      "OFPXMT_OFB_ARP_THA" : 25,
      "OFPXMT_OFB_IPV6_SRC" : 26,
      "OFPXMT_OFB_IPV6_DST" : 27,
      "OFPXMT_OFB_IPV6_FLABEL" : 28,
      "OFPXMT_OFB_ICMPV6_TYPE" : 29,
      "OFPXMT_OFB_ICMPV6_CODE" : 30,
      "OFPXMT_OFB_IPV6_ND_TARGET" : 31,
      "OFPXMT_OFB_IPV6_ND_SLL" : 32,
      "OFPXMT_OFB_IPV6_ND_TLL" : 33,
      "OFPXMT_OFB_MPLS_LABEL" : 34,
      "OFPXMT_OFB_MPLS_TC" : 35,
    }
    testobj = "ofp_oxm_ofb_match_field"
    self.runtests(testpairs, testobj)
  
  def test_ofp_vlan_id(self):
    testpairs = {
      "OFPVID_PRESENT" : 0x1000,
      "OFPVID_NONE" : 0x0000,
    }
    testobj = "ofp_vlan_id"
    self.runtests(testpairs, testobj)
  
  def test_ofp_instruction_type(self):
    testpairs = {
      "OFPIT_GOTO_TABLE" : 1,
      "OFPIT_WRITE_METADATA" : 2,
      "OFPIT_WRITE_ACTIONS" : 3,
      "OFPIT_APPLY_ACTIONS" : 4,
      "OFPIT_CLEAR_ACTIONS" : 5,
      "OFPIT_EXPERIMENTER" : 0xFFFF,
    }
    testobj = "ofp_instruction_type"
    self.runtests(testpairs, testobj)
  
  def test_ofp_action_type(self):
    testpairs = {
      "OFPAT_OUTPUT" : 1,
      "OFPAT_COPY_TTL_OUT" : 11,
      "OFPAT_COPY_TTL_IN" : 12,
      "OFPAT_SET_MPLS_TTL" : 15,
      "OFPAT_DEC_MPLS_TTL" : 16,
      "OFPAT_PUSH_VLAN" : 17,
      "OFPAT_POP_VLAN" : 18,
      "OFPAT_PUSH_MPLS" : 19,
      "OFPAT_POP_MPLS" : 20,
      "OFPAT_SET_QUEUE" : 21,
      "OFPAT_GROUP" : 22,
      "OFPAT_SET_NW_TTL" : 23,
      "OFPAT_DEC_NW_TTL" : 24,
      "OFPAT_SET_FIELD" : 25,
      "OFPAT_EXPERIMENTER" : 0xffff,
    }
    testobj = "ofp_action_type"
    self.runtests(testpairs, testobj)
  
  def test_ofp_controller_max_len(self):
    testpairs = {
      "OFPCML_MAX" : 0xffe5,
      "OFPCML_NO_BUFFER" : 0xffff,
    }
    testobj = "ofp_controller_max_len"
    self.runtests(testpairs, testobj)
  
  def test_ofp_capabilities(self):
    testpairs = {
      "OFPC_FLOW_STATS" : 0,
      "OFPC_TABLE_STATS" : 1,
      "OFPC_PORT_STATS" : 2,
      "OFPC_GROUP_STATS" : 3,
      "OFPC_IP_REASM" : 5,
      "OFPC_QUEUE_STATS" : 6,
      "OFPC_PORT_BLOCKED" : 8,
    }
    testobj = "ofp_capabilities"
    self.runtests(testpairs, testobj)
  
  def test_ofp_config_flags(self):
    testpairs = {
      "OFPC_FRAG_NORMAL" : 0,
      "OFPC_FRAG_DROP" : 1 << 0,
      "OFPC_FRAG_REASM" : 1 << 1,
      "OFPC_FRAG_MASK" : 3,
      "OFPC_INVALID_TTL_TO_CONTROLLER" : 1 << 2,
    }
    testobj = "ofp_config_flags"
    self.runtests(testpairs, testobj)
  
  def test_ofp_table(self):
    testpairs = {
      "OFPTT_MAX" : 0xfe,
      "OFPTT_ALL" : 0xff,
    }
    testobj = "ofp_table"
    self.runtests(testpairs, testobj)
  
  def test_ofp_table_config(self):
    testpairs = {
      "OFPTC_TABLE_MISS_CONTROLLER" : 0,
      "OFPTC_TABLE_MISS_CONTINUE" : 1 << 0,
      "OFPTC_TABLE_MISS_DROP" : 1 << 1,
      "OFPTC_TABLE_MISS_MASK" : 3,
    }
    testobj = "ofp_table_config"
    self.runtests(testpairs, testobj)
  
  def test_ofp_flow_mod_command(self):
    testpairs = {
      "OFPFC_ADD" : 0,
      "OFPFC_MODIFY" : 1,
      "OFPFC_MODIFY_STRICT" : 2,
      "OFPFC_DELETE" : 3,
      "OFPFC_DELETE_STRICT" : 4,
    }
    testobj = "ofp_flow_mod_command"
    self.runtests(testpairs, testobj)
  
  def test_ofp_flow_mod_flags(self):
    testpairs = {
      "OFPFF_SEND_FLOW_REM" : 1 << 0,
      "OFPFF_CHECK_OVERLAP" : 1 << 1,
      "OFPFF_RESET_COUNTS" : 1 << 2,
    }
    testobj = "ofp_flow_mod_flags"
    self.runtests(testpairs, testobj)
  
  def test_ofp_flow_mod_flags(self):
    testpairs = {
      "OFPFF_SEND_FLOW_REM" : 1 << 0,
      "OFPFF_CHECK_OVERLAP" : 1 << 1,
      "OFPFF_RESET_COUNTS" : 1 << 2,
    }
    testobj = "ofp_flow_mod_flags"
    self.runtests(testpairs, testobj)
  
  def test_ofp_group_mod_command(self):
    testpairs = {
      "OFPGC_ADD" : 0,
      "OFPGC_MODIFY" : 1,
      "OFPGC_DELETE" : 2,
    }
    testobj = "ofp_group_mod_command"
    self.runtests(testpairs, testobj)
  
  def test_ofp_group_type(self):
    testpairs = {
      "OFPGT_ALL" : 0,
      "OFPGT_SELECT" : 1,
      "OFPGT_INDIRECT" : 2,
      "OFPGT_FF" : 3,
    }
    testobj = "ofp_group_type"
    self.runtests(testpairs, testobj)
  
  def test_ofp_stats_types(self):
    testpairs = {
      "OFPST_DESC" : 0,
      "OFPST_FLOW" : 1,
      "OFPST_AGGREGATE" : 2,
      "OFPST_TABLE" : 3,
      "OFPST_PORT" : 4,
      "OFPST_QUEUE" : 5,
      "OFPST_GROUP" : 6,
      "OFPST_GROUP_DESC" : 7,
      "OFPST_GROUP_FEATURES" : 8,
      "OFPST_EXPERIMENTER" : 0xffff,
    }
    testobj = "ofp_stats_types"
    self.runtests(testpairs, testobj)
  
  def test_ofp_group_capabilities(self):
    testpairs = {
      "OFPGFC_SELECT_WEIGHT" : 1 << 0,
      "OFPGFC_SELECT_LIVENESS" : 1 << 1,
      "OFPGFC_CHAINING" : 1 << 2,
      "OFPGFC_CHAINING_CHECKS" : 1 << 3,
    }
    testobj = "ofp_group_capabilities"
    self.runtests(testpairs, testobj)
  
  def test_ofp_controller_role(self):
    testpairs = {
      "OFPCR_ROLE_NOCHANGE" : 0,
      "OFPCR_ROLE_EQUAL" : 1,
      "OFPCR_ROLE_MASTER" : 2,
      "OFPCR_ROLE_SLAVE" : 3,
    }
    testobj = "ofp_controller_role"
    self.runtests(testpairs, testobj)
  
  def test_ofp_packet_in_reason(self):
    testpairs = {
      "OFPR_NO_MATCH" : 0,
      "OFPR_ACTION" : 1,
      "OFPR_INVALID_TTL" : 2,
    }
    testobj = "ofp_packet_in_reason"
    self.runtests(testpairs, testobj)
  
  def test_ofp_flow_removed_reason(self):
    testpairs = {
      "OFPRR_IDLE_TIMEOUT" : 0,
      "OFPRR_HARD_TIMEOUT" : 1,
      "OFPRR_DELETE" : 2,
      "OFPRR_GROUP_DELETE" : 3,
    }
    testobj = "ofp_flow_removed_reason"
    self.runtests(testpairs, testobj)
  
  def test_ofp_port_reason(self):
    testpairs = {
      "OFPPR_ADD" : 0,
      "OFPPR_DELETE" : 1,
      "OFPPR_MODIFY" : 2,
    }
    testobj = "ofp_port_reason"
    self.runtests(testpairs, testobj)
  
  def test_ofp_error_type(self):
    testpairs = {
      "OFPET_HELLO_FAILED" : 0,
      "OFPET_BAD_REQUEST" : 1,
      "OFPET_BAD_ACTION" : 2,
      "OFPET_BAD_INSTRUCTION" : 3,
      "OFPET_BAD_MATCH" : 4,
      "OFPET_FLOW_MOD_FAILED" : 5,
      "OFPET_GROUP_MOD_FAILED" : 6,
      "OFPET_PORT_MOD_FAILED" : 7,
      "OFPET_TABLE_MOD_FAILED" : 8,
      "OFPET_QUEUE_OP_FAILED" : 9,
      "OFPET_SWITCH_CONFIG_FAILED" : 10,
      "OFPET_ROLE_REQUEST_FAILED" : 11,
      "OFPET_EXPERIMENTER" : 0xffff,
    }
    testobj = "ofp_error_type"
    self.runtests(testpairs, testobj)
  
  def test_ofp_hello_failed_code(self):
    testpairs = {
      "OFPHFC_INCOMPATIBLE" : 0,
      "OFPHFC_EPERM" : 1,
    }
    testobj = "ofp_hello_failed_code"
    self.runtests(testpairs, testobj)
  
  def test_ofp_bad_request_code(self):
    testpairs = {
      "OFPBRC_BAD_VERSION" : 0,
      "OFPBRC_BAD_TYPE" : 1,
      "OFPBRC_BAD_STAT" : 2,
      "OFPBRC_BAD_EXPERIMENTER" : 3,
      "OFPBRC_BAD_EXP_TYPE" : 4,
      "OFPBRC_EPERM" : 5,
      "OFPBRC_BAD_LEN" : 6,
      "OFPBRC_BUFFER_EMPTY" : 7,
      "OFPBRC_BUFFER_UNKNOWN" : 8,
      "OFPBRC_BAD_TABLE_ID" : 9,
      "OFPBRC_IS_SLAVE" : 10,
      "OFPBRC_BAD_PORT" : 11,
      "OFPBRC_BAD_PACKET" : 12,
    }
    testobj = "ofp_bad_request_code"
    self.runtests(testpairs, testobj)
  
  def test_ofp_bad_instruction_code(self):
    testpairs = {
      "OFPBIC_UNKNOWN_LIST" : 0,
      "OFPBIC_UNSUP_INST" : 1,
      "OFPBIC_BAD_TABLE_ID" : 2,
      "OFPBIC_UNSUP_METADATA" : 3,
      "OFPBIC_UNSUP_METADATA_MASK" : 4,
      "OFPBIC_BAD_EXPERIMENTER" : 5,
      "OFPBIC_BAD_EXP_TYPE" : 6,
      "OFPBIC_BAD_LEN" : 7,
      "OFPBIC_EPERM" : 8,
    }
    testobj = "ofp_bad_instruction_code"
    self.runtests(testpairs, testobj)
  
  def test_ofp_bad_match_code(self):
    testpairs = {
      "OFPBMC_BAD_TYPE" : 0,
      "OFPBMC_BAD_LEN" : 1,
      "OFPBMC_BAD_TAG" : 2,
      "OFPBMC_BAD_DL_ADDR_MASK" : 3,
      "OFPBMC_BAD_NW_ADDR_MASK" : 4,
      "OFPBMC_BAD_WILDCARDS" : 5,
      "OFPBMC_BAD_FIELD" : 6,
      "OFPBMC_BAD_VALUE" : 7,
      "OFPBMC_BAD_MASK" : 8,
      "OFPBMC_BAD_PREREQ" : 9,
      "OFPBMC_DUP_FIELD" : 10,
      "OFPBMC_EPERM" : 11,
    }
    testobj = "ofp_bad_match_code"
    self.runtests(testpairs, testobj)
  
  def test_ofp_flow_mod_failed_code(self):
    testpairs = {
      "OFPFMFC_UNKNOWN" : 0,
      "OFPFMFC_TABLE_FULL" : 1,
      "OFPFMFC_BAD_TABLE_ID" : 2,
      "OFPFMFC_OVERLAP" : 3,
      "OFPFMFC_EPERM" : 4,
      "OFPFMFC_BAD_TIMEOUT" : 5,
      "OFPFMFC_BAD_COMMAND" : 6,
      "OFPFMFC_BAD_FLAGS" : 7,
    }
    testobj = "ofp_flow_mod_failed_code"
    self.runtests(testpairs, testobj)
  
  def test_ofp_group_mod_failed_code(self):
    testpairs = {
      "OFPGMFC_GROUP_EXISTS" : 0,
      "OFPGMFC_INVALID_GROUP" : 1,
      "OFPGMFC_WEIGHT_UNSUPPORTED" : 2,
      "OFPGMFC_OUT_OF_GROUPS" : 3,
      "OFPGMFC_OUT_OF_BUCKETS" : 4,
      "OFPGMFC_CHAINING_UNSUPPORTED" : 5,
      "OFPGMFC_WATCH_UNSUPPORTED" : 6,
      "OFPGMFC_LOOP" : 7,
      "OFPGMFC_UNKNOWN_GROUP" : 8,
      "OFPGMFC_CHAINED_GROUP" : 9,
      "OFPGMFC_BAD_TYPE" : 10,
      "OFPGMFC_BAD_COMMAND" : 11,
      "OFPGMFC_BAD_BUCKET" : 12,
      "OFPGMFC_BAD_WATCH" : 13,
      "OFPGMFC_EPERM" : 14,
    }
    testobj = "ofp_group_mod_failed_code"
    self.runtests(testpairs, testobj)
  
  def test_ofp_port_mod_failed_code(self):
    testpairs = {
      "OFPPMFC_BAD_PORT" : 0,
      "OFPPMFC_BAD_HW_ADDR" : 1,
      "OFPPMFC_BAD_CONFIG" : 2,
      "OFPPMFC_BAD_ADVERTISE" : 3,
      "OFPPMFC_EPERM" : 4,
    }
    testobj = "ofp_port_mod_failed_code"
    self.runtests(testpairs, testobj)
  
  def test_ofp_table_mod_failed_code(self):
    testpairs = {
      "OFPTMFC_BAD_TABLE" : 0,
      "OFPTMFC_BAD_CONFIG" : 1,
      "OFPTMFC_EPERM" : 2,
    }
    testobj = "ofp_table_mod_failed_code"
    self.runtests(testpairs, testobj)
  
  def test_ofp_queue_op_failed_code(self):
    testpairs = {
      "OFPQOFC_BAD_PORT" : 0,
      "OFPQOFC_BAD_QUEUE" : 1,
      "OFPQOFC_EPERM" : 2,
    }
    testobj = "ofp_queue_op_failed_code"
    self.runtests(testpairs, testobj)
  
  def test_ofp_switch_config_failed_code(self):
    testpairs = {
      "OFPSCFC_BAD_FLAGS" : 0,
      "OFPSCFC_BAD_LEN" : 1,
      "OFPSCFC_EPERM" : 2,
    }
    testobj = "ofp_switch_config_failed_code"
    self.runtests(testpairs, testobj)
  
  def test_ofp_role_request_failed_code(self):
    testpairs = {
      "OFPRRF_STALE" : 0,
      "OFPRRF_UNSUP" : 1,
      "OFPRRF_BAD_ROLE" : 2,
    }
    testobj = "ofp_role_request_failed_code"
    self.runtests(testpairs, testobj)
  
  def test_ofp_error_experimenter_msg(self):
    testpairs = {
      "OFPRRF_STALE" : 0,
      "OFPRRF_UNSUP" : 1,
      "OFPRRF_BAD_ROLE" : 2,
    }
    testobj = "ofp_role_request_failed_code"
    self.runtests(testpairs, testobj)


class ofp_match_test(unittest.TestCase):
  
  def test_mpls_match(self):
    
    # create packet first
    # ping packet taken from wireshark pcap samples
    pkt = ""
    # ethernet
    dl_dst = EthAddr(b"\x00\x30\x96\xe6\xfc\x39")
    dl_src = EthAddr(b"\x00\x30\x96\x05\x28\x38")
    eth_type = 0x8847
    pkt += dl_dst.toRaw()
    pkt += dl_src.toRaw()
    pkt += struct.pack("!H", eth_type)
    # MPLS
    mpls_label = 29
    mpls_tc = 0
    mpls_ttl = 0xff
    mpls_label_top = mpls_label >> 4
    mpls_label_bottom = mpls_label & 0xF
    pkt += struct.pack("!HBB", mpls_label_top, (mpls_label_bottom << 4) + (mpls_tc << 1) + 1, 0xff)
    # IP
    nw_proto = 1
    nw_tos = 0
    nw_src = IPAddr("10.1.2.1")
    nw_dst = IPAddr("10.34.0.1")
    pkt += struct.pack("!BBHHBBBBHLL", 0x45, nw_tos, 0x0064, 0x000a, 0x00, 0x00, 0xff, nw_proto, 0xa56a, nw_src.toUnsigned(), nw_dst.toUnsigned())
    # ICMP
    pkt += struct.pack("!BBHHH", 0x08, 0x00, 0x3a77, 0x0a39, 0x062b)
    pkt += struct.pack("!BBBBBBBB", 0x00, 0x00, 0x00, 0x00, 0x00, 0x1f, 0x33, 0x50)
    for i in range(0, 31):
      pkt += struct.pack("!H", 0xabcd)
    #
    #for i in range(0, 3):
    #  row = struct.unpack_from("!BBBBBBBBBBBBBBBB",pkt, i*16)
    #  print "%X %X %X %X %X %X %X %X %X %X %X %X %X %X %X %X" % ( row[0],
    #    row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], 
    #    row[10], row[11], row[12], row[13], row[14], row[15]) 
    packet = ethernet(pkt)
    # create match from packet
    match = ofp_match.from_packet(packet)
    
    #print match.dl_src
    #print match.dl_src_mask
    #print match.dl_dst
    #print match.dl_dst_mask
    #print match.nw_src
    #print match.nw_src_mask
    #print match.nw_dst
    #print match.nw_dst_mask
    #print match.mpls_label
    #print match.mpls_tc
    
    self.assertEquals(match.dl_src, dl_src)
    self.assertEquals(match.dl_dst, dl_dst)
    self.assertEquals(match.nw_src, nw_src)
    self.assertEquals(match.nw_dst, nw_dst)
    self.assertEquals(match.mpls_label, mpls_label)
    self.assertEquals(match.mpls_tc, mpls_tc)
  
  def test_bit_wildcards(self):
    """ some checking of the bit-level wildcard magic in ofp_match"""
    m = ofp_match()

    # all match entries should start out as wildcarded
    for k,v in ofp_match_data.iteritems():
         self.assertEquals(getattr(m, k), None, "Attr %s should be wildcarded and reported as None" % k)
         self.assertEquals(m.wildcards & v[1], v[1])

    # try setting and unsetting specific bit-level match entries
    for change in [ ("in_port", 1, OFPFW_IN_PORT), ("dl_vlan", 2, OFPFW_DL_VLAN), ("tp_dst", 22, OFPFW_TP_DST) ]:
      setattr(m, change[0], change[1])
      self.assertEquals(getattr(m, change[0]), change[1], "Attr %s should have been set to %s" % change[0:2])
      self.assertEquals(m.wildcards & change[2], 0, "with %s set to %s, wildcard bit %x should get unset" % change)
      setattr(m, change[0], None)
      self.assertEquals(m.wildcards & change[2], change[2], "with %s reset from %s, wildcard bit %x should be set again" % change)

  #def test_ip_wildcard_magic(self):
    # this is meaningless for openflow 1.1
    """ ofp_match: check IP wildcard magic"""

    # do this for both nw_src and nw_dst
    #for (attr, bitmask, shift) in ( ("nw_src", OFPFW_NW_SRC_MASK, OFPFW_NW_SRC_SHIFT), ( "nw_dst", OFPFW_NW_DST_MASK, OFPFW_NW_DST_SHIFT) ):
    #  m = ofp_match()
      #self.assertEquals(getattr(m, "get_"+attr)(), (None, 0), "get_%s for unset %s should return (None,0)" % (attr, attr))

      #self.assertTrue( ((m.wildcards & bitmask) >> shift) >= 32)

      ## set a bunch of ip addresses with or without networks
      #for ipnet in ( "10.0.0.0/8", "172.16.0.0/16", "192.168.24.0/24", "1.2.3.4/30", "212.11.225.3"):
        #parts = ipnet.split("/")
        #ip = parts[0]
        #bits = int(parts[1]) if len(parts)>1 else 32
        ## set the IP address
        #setattr(m, attr, ipnet)

        ## gets converted to just the ip address during query
        #self.assertEqual(getattr(m, attr), ip)

        ## the get_#{attr} method gives a tuple of (ip, cidr-bits)
        #self.assertEqual( getattr(m, "get_"+attr)(), (ip, bits))

        ## the appropriate bits in the wildcard should be set
        #self.assertEqual( (m.wildcards & bitmask) >> shift, 32-bits)

      ## reset to 0.0.0.0/0 results in full wildcard
      #setattr(m, attr, "0.0.0.0/0")
      #self.assertEquals(getattr(m, "get_"+attr)(), (None, 0), "get_%s for unset %s should return (None,0)" % (attr, attr))
      #self.assertTrue( ((m.wildcards & bitmask) >> shift) >= 32)

  def test_match_with_wildcards(self):
    """ ofp_match: test the matches_with_wildcards method """
    def create(wildcards=(), **kw):
      m = ofp_match(in_port=1, dl_type=0, dl_src=EthAddr("00:00:00:00:00:01"), dl_dst=EthAddr("00:00:00:00:00:02"), dl_vlan=5, nw_proto=6, nw_src="10.0.0.1", nw_dst="11.0.0.1", tp_src = 12345, tp_dst=80)

      if isinstance(wildcards, str):
        wildcards = [wildcards]

      for w in wildcards:
        setattr(m, w, None)

      for (k,v) in kw.iteritems():
        m.__setattr__(k,v)
      return m

    def assertMatch(ref, other, msg=""):
      self.assertTrue(ref.matches_with_wildcards(other), "%s - %s should match %s " % (msg, ref.show(), other.show()))

    def assertNoMatch(ref, other, msg=""):
      self.assertFalse(ref.matches_with_wildcards(other), "%s - %s should NOT match %s " % (msg, ref.show(), other.show()))

    ref = create()
    print ref

    # same instances match
    assertMatch(ref, ref)
    # equal instances match
    assertMatch(ref, create())

    # ofp_match with additional wildcard bits set match the ref, but not the other way round
    for wildcards in ( [ "in_port" ], [ "dl_vlan" ], [ "dl_src", "dl_dst" ] ):
      wilder = create(wildcards=wildcards)
      assertMatch(wilder, ref)
      assertNoMatch(ref, wilder)

    # when fields are wildcarded, we can change around the actual values and it will still match
    for changes in ( { "in_port": 15 }, { "dl_src": "12:34:56:78:90:ab", "dl_vlan": 7 }, { "tp_dst" : 22 } ):
      wild = create()
      concrete = create()
      for (k,v) in changes.iteritems():
        setattr(wild, k, None)
        setattr(concrete, k, v)
      assertMatch(wild, concrete)
      assertNoMatch(concrete, wild)

    # play around with nw src addresses
    assertMatch(create(nw_src="10.0.0.0/24"), ref)
    assertMatch(create(nw_src="10.0.0.0/24"), create(nw_src="10.0.0.0/25"))
    assertNoMatch(create(nw_src="10.0.0.0/25"), create(nw_src="10.0.0.0/24"))
    assertMatch(create(nw_src="10.0.0.0/25"), create(nw_src="10.0.0.127"))
    assertNoMatch(create(nw_src="10.0.0.0/25"), create(nw_src="10.0.0.128"))

# needs to be updated for openflow 1.1
# double-check that this is all of the messages
class ofp_command_test(unittest.TestCase):
  # custom map of POX class to header type, for validation
  ofp_type = {
    ofp_features_reply: OFPT_FEATURES_REPLY,
    ofp_switch_config: OFPT_SET_CONFIG,
    ofp_flow_mod: OFPT_FLOW_MOD,
    ofp_port_mod: OFPT_PORT_MOD,
    ofp_queue_get_config_request: OFPT_QUEUE_GET_CONFIG_REQUEST,
    ofp_queue_get_config_reply: OFPT_QUEUE_GET_CONFIG_REPLY,
    ofp_stats_request: OFPT_STATS_REQUEST,
    ofp_stats_reply: OFPT_STATS_REPLY,
    ofp_packet_out: OFPT_PACKET_OUT,
    ofp_barrier_reply: OFPT_BARRIER_REPLY,
    ofp_barrier_request: OFPT_BARRIER_REQUEST,
    ofp_packet_in: OFPT_PACKET_IN,
    ofp_flow_removed: OFPT_FLOW_REMOVED,
    ofp_port_status: OFPT_PORT_STATUS,
    ofp_error: OFPT_ERROR,
    ofp_hello: OFPT_HELLO,
    ofp_echo_request: OFPT_ECHO_REQUEST,
    ofp_echo_reply: OFPT_ECHO_REPLY,
    ofp_features_request: OFPT_FEATURES_REQUEST,
    ofp_get_config_request: OFPT_GET_CONFIG_REQUEST,
    ofp_get_config_reply: OFPT_GET_CONFIG_REPLY,
    ofp_set_config: OFPT_SET_CONFIG
    }
    
    
  def test_mpls_tag_swap(self):
    # we want to create a flow to match on mpls tags and make sure it works
    # match on tag 45, make it swap to tag 23 and output on port 4
    msg = ofp_flow_mod(xid=2)
    msg.match.mpls_label = 45
    
    action_tagswap = ofp_action_mpls_label(mpls_label = 23)
    action_output = ofp_action_output(port = 4)
    # set up instruction now that we have actions
    instruction = ofp_instruction_actions.apply_actions(actions = [action_tagswap, action_output])
    msg.instructions.append(instruction)

    # try packing and unpacking msg?
    self._test_pack_unpack(msg, 2)

# need to test mpls tag pushing and popping too

  def assert_packed_header(self, pack, ofp_type, length, xid):
    """ check openflow header fields in packed byte array """
    # should be updated to of1.2
    def assert_num(name, start, length, expected):
      val = extract_num(pack, start, length)
      self.assertEquals(val, expected, "packed header check: %s for ofp type %s should be %d (is %d)" % (name, ofp_type_map[ofp_type], expected, val))

    assert_num("OpenFlow version", 0, 1, 3)
    assert_num("header_type", 1, 1, ofp_type)
    assert_num("length in header", 2, 2, length)
    assert_num("xid", 4, 4, xid)

  def _test_pack_unpack(self, o, xid, ofp_type=None):
    """ check that packing and unpacking an ofp object works, and that lengths etc. are correct """
    show = lambda(o): o.show() if hasattr(o, "show") else str(show)

    if not ofp_type:
      ofp_type = self.ofp_type[type(o)]

    self.assertTrue(o._assert(), "pack_unpack for %s -- original object should _assert to true"%show(o))
    # show the object to make sure that works
    o.show()
    # pack object
    pack = o.pack()
    # byte array length should equal calculated length
    self.assertEqual(len(o), len(pack), "pack_unpack for %s -- len(object)=%d != len(packed)=%d" % (type(o), len(o), len(pack)))
    # check header fields in packed byte array
    self.assert_packed_header(pack, ofp_type, len(o), xid)
    # now unpack
    unpacked = type(o)()
    unpacked.unpack(pack)
    self.assertEqual(o, unpacked, "pack_unpacked -- original != unpacked\n===Original:\n%s\n===Repacked:%s\n" % (show(o), show(unpacked)))
    return unpacked

  def test_header_pack_unpack(self):
    for kw in ( { "header_type": OFPT_PACKET_OUT, "xid": 1 },
                { "header_type": OFPT_FLOW_MOD, "xid": 2 }):
      # Can't directly pack a header, since it has no length...
      class H (ofp_header):
        def __len__ (self):
          return 8
      o = H(**kw)
      self._test_pack_unpack(o, kw["xid"], kw["header_type"])

  def test_pack_all_comands_simple(self):
    xid_gen = itertools.count()
    for cls in ( ofp_features_reply,
                   ofp_switch_config,
                   ofp_flow_mod,
                   ofp_port_mod,
                   ofp_queue_get_config_request,
                   ofp_queue_get_config_reply,
                   ofp_stats_request,
                   ofp_stats_reply,
                   ofp_packet_out,
                   ofp_barrier_reply,
                   ofp_barrier_request,
                   ofp_packet_in,
                   ofp_flow_removed,
                   ofp_port_status,
                   ofp_error,
                   ofp_hello,
                   ofp_echo_request,
                   ofp_echo_reply,
                   ofp_features_request,
                   ofp_get_config_request,
                   ofp_get_config_reply,
                   ofp_set_config ):
      xid = xid_gen.next()
      args = {}

      # Customize initializer
      if cls in (ofp_stats_reply, ofp_stats_request):
        # These need a body set
        args['body'] = ofp_desc_stats(sw_desc="POX")

      o = cls(xid=xid, **args)
      self._test_pack_unpack(o, xid)

  out = ofp_action_output
  dl_addr = ofp_action_dl_addr
  some_actions = ([], [out(port=2)], [out(port=2), out(port=3)], [ out(port=OFPP_FLOOD) ], [ dl_addr.set_dst(EthAddr("00:"*5 + "01")), out(port=1) ])


  def test_pack_custom_packet_out(self):
    xid_gen = xid_generator()
    packet = ethernet(src=EthAddr("00:00:00:00:00:01"), dst=EthAddr("00:00:00:00:00:02"),
            payload=ipv4(srcip=IPAddr("1.2.3.4"), dstip=IPAddr("1.2.3.5"),
                payload=udp(srcport=1234, dstport=53, payload="haha"))).pack()

    for actions in self.some_actions:
      for attrs in ( { 'data': packet }, { 'buffer_id': 5 } ):
        xid = xid_gen()
        o = ofp_packet_out(xid=xid, actions=actions, **attrs)
        self._test_pack_unpack(o, xid, OFPT_PACKET_OUT)

  def test_pack_flow_mod_openflow_dl_type_wildcards(self):
    """ Openflow 1.1 spec clarifies that wildcards should not be set when the protocol in
        question is not matched i.e., dl_type != 0x800 -> no wildcards for IP.
        Test this here """
    def show_wildcards(w):
      parts = [ k.lower()[len("OFPFW_"):] for (k,v) in ofp_flow_wildcards_rev_map.iteritems() if v & w == v ]
      #nw_src_bits = (w & OFPFW_NW_SRC_MASK) >> OFPFW_NW_SRC_SHIFT
      #nw_src_bits = (w & OFPFW_NW_SRC_MASK) >> OFPFW_NW_SRC_SHIFT
      nw_src_bits = 0
      if(nw_src_bits > 0): parts.append("nw_src(/%d)" % (32 - nw_src_bits))

      #nw_dst_bits = (w & OFPFW_NW_DST_MASK) >> OFPFW_NW_DST_SHIFT
      nw_dst_bits = 0
      if(nw_dst_bits > 0): parts.append("nw_dst(/%d)" % (32 - nw_dst_bits))
      return "|".join(parts)

    def test_wildcards(match, expected):
      (packed,) = struct.unpack_from("!L", match.pack(flow_mod=True))
      self.assertEquals(packed, expected, "packed: %s <> expected: %s" % (show_wildcards(packed), show_wildcards(expected)))

    # no dl type specified -> wildcards for nw/dl are cleared
    # deleted OFPFW_NW_SRC_MASK | OFPFW_NW_DST_MASK - these need to be set in a different way now
    test_wildcards(ofp_match(), OFPFW_ALL & ~ (OFPFW_NW_TOS | OFPFW_NW_PROTO |  OFPFW_TP_SRC | OFPFW_TP_DST))
    all_normalized = (OFPFW_ALL & ~ (OFPFW_NW_SRC_MASK | OFPFW_NW_DST_MASK)) | \
            OFPFW_NW_SRC_ALL | OFPFW_NW_DST_ALL

    # dl type = ARP -> certain wildcards live
    test_wildcards(ofp_match(dl_type=0x806), all_normalized & ~ (OFPFW_NW_TOS | OFPFW_TP_SRC | OFPFW_TP_DST | OFPFW_DL_TYPE))
    # dl type = IP -> more wildcards live
    test_wildcards(ofp_match(dl_type=0x800), all_normalized & ~ (OFPFW_TP_SRC | OFPFW_TP_DST | OFPFW_DL_TYPE))
    # dl type = IP, nw_proto=UDP -> alll wildcards live
    test_wildcards(ofp_match(dl_type=0x800,nw_proto=6), all_normalized & ~(OFPFW_DL_TYPE | OFPFW_NW_PROTO))


  def test_pack_custom_flow_mod(self):
    out = ofp_action_output
    xid_gen = xid_generator()

    for match in ( ofp_match(),
        ofp_match(in_port=1, dl_type=0x88cc, dl_src=EthAddr("00:00:00:00:00:01"), dl_dst=EthAddr("00:00:00:00:00:02")),
        ofp_match(in_port=1, dl_type=0x0806, dl_src=EthAddr("00:00:00:00:00:01"), dl_dst=EthAddr("00:00:00:00:00:02"), nw_src="10.0.0.1", nw_dst="11.0.0.1"),
        ofp_match(in_port=1, dl_type=0x0800, dl_src=EthAddr("00:00:00:00:00:01"), dl_dst=EthAddr("00:00:00:00:00:02"), dl_vlan=5, nw_proto=6, nw_src="10.0.0.1", nw_dst="11.0.0.1", tp_src = 12345, tp_dst=80)):
      for actions in self.some_actions:
        for command in ( OFPFC_ADD, OFPFC_DELETE, OFPFC_DELETE_STRICT, OFPFC_MODIFY_STRICT, OFPFC_MODIFY_STRICT ):
          for attrs in ( {}, { 'buffer_id' : 123 }, { 'idle_timeout': 5, 'hard_timeout': 10 } ):
            xid = xid_gen()
            # just wrap actions in OFPIT_APPLY_ACTIONS for the time being
            instruction1 = ofp_instruction_actions.apply_actions(actions)
            instructions = [instruction1]
            o = ofp_flow_mod(xid=xid, command=command, match = match, instructions=instructions, **attrs)
            # test the instructions
            unpacked = self._test_pack_unpack(o, xid, OFPT_FLOW_MOD)

            self.assertEqual(unpacked.match, match)
            self.assertEqual(unpacked.command, command)
            self.assertEqual(unpacked.instructions, instructions)
            for (check_attr,val) in attrs.iteritems():
              self.assertEqual(getattr(unpacked, check_attr), val)

class ofp_action_test(unittest.TestCase):
  def assert_packed_action(self, cls, packed, a_type, length):
    self.assertEqual(extract_num(packed, 0,2), a_type, "Action %s: expected type %d (but is %d)" % (cls, a_type, extract_num(packed, 0,2)))
    self.assertEqual(extract_num(packed, 2,2), length, "Action %s: expected length %d (but is %d)" % (cls, length, extract_num(packed, 2,2)))

  def test_pack_all_actions_simple(self):
    def c(cls, a_type, kw, length):
      action = cls(**kw)
      packed = action.pack()
      self.assertEqual(len(action), len(packed))
      self.assert_packed_action(cls, packed, a_type, length)
      unpacked = cls()
      unpacked.unpack(packed)
      self.assertEqual(action, unpacked)
      for (k, v) in kw.iteritems():
        self.assertEqual(getattr(unpacked, k), v)
      return packed


    # needs updating for openflow 1.1
    # add all of the new actions (MPLS etc)
    # 16-byte ofp_action_output in openflow 1.1
    c(ofp_action_output, OFPAT_OUTPUT, { 'port': 23 }, 16 )
    c(ofp_action_set_queue, OFPAT_SET_QUEUE, { 'queue_id': 1 }, 8 )
    c(ofp_action_vlan_vid, OFPAT_SET_VLAN_VID, { 'vlan_vid' : 123}, 8 )
    c(ofp_action_vlan_pcp, OFPAT_SET_VLAN_PCP, { 'vlan_pcp' : 123}, 8 )
    p = c(ofp_action_dl_addr.set_dst, OFPAT_SET_DL_DST, { 'dl_addr' : EthAddr("01:02:03:04:05:06").toRaw() }, 16 )
    self.assertEquals(extract_num(p, 4,6), 0x010203040506)
    p = c(ofp_action_dl_addr.set_src, OFPAT_SET_DL_SRC, { 'dl_addr' : EthAddr("ff:ee:dd:cc:bb:aa").toRaw() }, 16 )
    self.assertEquals(extract_num(p, 4,6), 0xffeeddccbbaa, "Ethernet in packed is %x, but should be ff:ee:dd:cc:bb:aa" % extract_num(p, 4, 6))
    p = c(ofp_action_nw_addr.set_dst, OFPAT_SET_NW_DST, { 'nw_addr' : IPAddr("1.2.3.4") }, 8 )
    self.assertEquals(extract_num(p, 4,4), 0x01020304)
    p = c(ofp_action_nw_addr.set_src, OFPAT_SET_NW_SRC, { 'nw_addr' : IPAddr("127.0.0.1") }, 8 )
    self.assertEquals(extract_num(p, 4,4), 0x7f000001)
    c(ofp_action_nw_tos, OFPAT_SET_NW_TOS, { 'nw_tos' : 4 }, 8)
    p = c(ofp_action_tp_port.set_dst, OFPAT_SET_TP_DST, { 'tp_port' : 80 }, 8)
    self.assertEquals(extract_num(p, 4,2), 80)
    p = c(ofp_action_tp_port.set_src, OFPAT_SET_TP_SRC, { 'tp_port' : 22987 }, 8)
    self.assertEquals(extract_num(p, 4,2), 22987)
#    c(ofp_action_push_mpls, OFPAT_PUSH_MPLS, {'ethertype':0x8847}, 8)
#    c(ofp_action_pop_mpls, OFPAT_POP_MPLS, {'ethertype':0x0800}, 8)
#    c(ofp_action_mpls_dec_ttl, OFPAT_DEC_MPLS_TTL, {}, 8)
#    c(ofp_action_mpls_label, OFPAT_SET_MPLS_LABEL, {'mpls_label': 0xa1f}, 8)
#    c(ofp_action_mpls_tc, OFPAT_SET_MPLS_TC, {'mpls_tc': 0xac}, 8)
#    c(ofp_action_mpls_ttl, OFPAT_SET_MPLS_TTL, {'mpls_ttl': 0xaf}, 8)

if __name__ == '__main__':
  unittest.main()
