import unittest
from ParkingLot import ParkingLot
class TestParkingLot(unittest.TestCase):

	def test_create_parking_lot(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		self.assertEqual(6,res)

	def test_park(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		self.assertNotEqual(-1,res)

	def test_leave(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.leave(1)
		self.assertEqual(True,res)

	def test_getRegNoFromColor(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.park("KA-01-HH-9999","White")
		regnos = parkingLot.getRegNoFromColor("White")
		self.assertIn("KA-01-HH-1234",regnos)
		self.assertIn("KA-01-HH-9999",regnos)

	def test_getSlotNoFromRegNo(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.park("KA-01-HH-9999","White")
		slotno = parkingLot.getSlotNoFromRegNo("KA-01-HH-9999")
		self.assertEqual(2,slotno)

	def test_getSlotNoFromColor(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.park("KA-01-HH-9999","White")
		slotnos = parkingLot.getSlotNoFromColor("White")
		self.assertIn("1",slotnos)
		self.assertIn("2",slotnos)

if __name__ == '__main__':
	unittest.main()
