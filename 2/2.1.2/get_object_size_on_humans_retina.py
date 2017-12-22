import argparse

"""
The distance from the center of the human's eye lens to retina
along the axis of view is approximately 17mm., and  range of change
in the focal length - from 14mm. to 17mm. (the last value corresponds
to the relaxed state of the ciliary muscle, when the eye is focused on
an object at a distance of more than 3 meters)
"""
FOCUS_DISTANCE = 17.


def get_object_size_on_humans_retina(distance_to_object, object_height, focus_distance):
    """
    Calculates an object size on human's retina
    based on the object remoteness and its height
    ============================================================
    The original formula is:
        object_height / distance_to_object = h / FOCUS_DISTANCE
    ============================================================
    :param distance_to_object: in meters
    :param object_height: in meters
    :return: object's size in mm
    """
    h = object_height / float(distance_to_object) * focus_distance
    return h


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--distance_to_object", default=100)
    parser.add_argument("-o", "--object_height", default=15)
    parser.add_argument("-f", "--focus_distance", default=FOCUS_DISTANCE)
    args = parser.parse_args()

    size = get_object_size_on_humans_retina(
        args.distance_to_object,
        args.object_height,
        args.focus_distance
    )
    print('Object size is {} mm'.format(size))
