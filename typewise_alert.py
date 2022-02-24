limit_defn = {
  'PASSIVE': {'lowerLimit': 0, 'upperLimit': 35},
  'HI_ACTIVE': {'lowerLimit': 0, 'upperLimit': 45},
  'MED_ACTIVE': {'lowerLimit': 0, 'upperLimit': 40},
}

warning = {
  'TOO_LOW': 'Hi, the temperature is too low',
  'TOO_HIGH': 'Hi, the temperature is too high',
  'NORMAL': 'Hi, Everything looks Fine'
}

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit = limit_defn[coolingType]['lowerLimit']
  upperLimit = limit_defn[coolingType]['upperLimit']
  return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(send_to_alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  return send_to_alertTarget(breachType)


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  return True


def send_to_email(breachType):
  recepient = "a.b@c.com"
  print(f'To: {recepient}')
  print(warning[breachType])
  return True
