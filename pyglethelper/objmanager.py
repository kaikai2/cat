class Object:
    def __init__(self) -> None:
        pass

    def activate(self) -> None:
        '''
        called when the object added to ObjectManager
        '''
        pass
    def deactivate(self) -> None:
        '''
        called when the object removed from ObjectManager
        '''
        pass

    def update(self) -> None:
        '''
        called if activated, every update on ObjectManager
        '''
        pass

class ObjectManager:
    def __init__(self) -> None:
        self.objs = []
        pass

    def add(self, obj: Object) -> None:
        self.objs.append(obj)
        obj.activate()

    def remove(self, obj: Object) -> None:
        obj.deactivate()
        self.objs.remove(obj)

    def update(self) -> None:
        for obj in self.objs:
            obj.update()