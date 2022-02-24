import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(120, 50, 100) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(75, 50, 100) == 'NORMAL')

  def test_classify_temperature_breach(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE', 30) == 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE', -20) == 'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE', 50) == 'TOO_HIGH')

  def test_check_and_alert_temp_inc(self):
    self.assertTrue(typewise_alert.check_and_alert(typewise_alert.send_to_controller,{'coolingType': 'PASSIVE'},30) == True)
    self.assertTrue(typewise_alert.check_and_alert(typewise_alert.send_to_email,{'coolingType': 'HI_ACTIVE'},50) == True)


if __name__ == '__main__':
  unittest.main()
