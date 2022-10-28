# O(nlog(n)) time | O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    blue_at_back = True if blueShirtHeights[-1] > redShirtHeights[-1] else False

    if blue_at_back:
        for idx in range(len(blueShirtHeights)):
            if not blueShirtHeights[idx] > redShirtHeights[idx]:
                return False
    else:
        for idx in range(len(blueShirtHeights)):
            if not redShirtHeights[idx] > blueShirtHeights[idx]:
                return False

    return True
