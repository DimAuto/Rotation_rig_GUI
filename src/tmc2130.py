
class TMC2130(object):
    def __init__(self, manager, addr) -> None:
        self.initial_angle = 0
        self.address = addr
        self.manager = manager
        self.direction = 0

    def setAddress(self, address):
        self.address = address

    def setInitAngle(self, angle):
        self.initial_angle = angle
    
    def setDirection(self, direction):
        self.direction = direction

    def rotate(self, speed, angle):
        if angle > 360:
            angle = 360
        if angle < 0:
            angle = 0
        angle = int(angle * 142.22222)
        speed = [speed & 0xff, (speed >> 8) & 0xff]
        steps = [angle & 0xff, (angle >> 8) & 0xff]
        dirc = [self.direction & 0xff, (self.direction >> 8) & 0xff]
        dc = [32, 0]
        data = steps + dirc + speed + dc
        self.manager.set_tx_data(data)
        self.manager.set_tx_cmd(self.address)
        self.manager.transmit_message()

    def disable_motor(self):
        self.manager.set_tx_data([0])
        self.manager.set_tx_cmd(self.address|0x02)
        self.manager.transmit_message()

    def enable_motor(self):
        self.manager.set_tx_data([0])
        self.manager.set_tx_cmd(self.address|0x01)
        self.manager.transmit_message()