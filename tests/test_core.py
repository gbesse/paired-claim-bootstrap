import unittest
from paired_claim_bootstrap import run
class DomainTests(unittest.TestCase):
 def test_constant_paired_gain(self):
  r=run({'pairs':[{'id':str(i),'a':i,'b':i+2} for i in range(5)]});self.assertEqual(r['paired_mean_b_minus_a'],2);self.assertEqual(r['percentile_interval'],[2,2])
 def test_pair_order_does_not_change_seeded_result(self):
  rows=[{'id':str(i),'a':0,'b':i,'block':str(i%2)} for i in range(6)];self.assertEqual(run({'pairs':rows}),run({'pairs':list(reversed(rows))}))
 def test_block_correlation_preserved(self):
  rows=[{'id':str(i),'a':0,'b':-1 if i<10 else 1,'block':'a' if i<10 else 'b'} for i in range(20)];r=run({'pairs':rows,'replicates':1000});self.assertEqual(r['percentile_interval'],[-1,1])
 def test_single_block_not_informative(self):
  r=run({'pairs':[{'id':'a','a':0,'b':1,'block':'one'},{'id':'b','a':0,'b':-1,'block':'one'}]});self.assertFalse(r['more_than_one_resampling_unit']);self.assertEqual(r['percentile_interval'],[0,0])
 def test_missing_pair_not_dropped_silently(self):
  with self.assertRaises(KeyError):run({'pairs':[{'id':'a','a':1}]})
