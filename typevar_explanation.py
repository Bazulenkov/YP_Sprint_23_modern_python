from typing import Type, TypeVar

T = TypeVar('T', bound="Geom")

class Geom:
    pass


class Point2D(Geom):
    pass


def factory_point(cls_geom: Type[T]) -> T:
    return cls_geom()


geom: Geom = factory_point(Geom)
point: Point2D = factory_point(Point2D)