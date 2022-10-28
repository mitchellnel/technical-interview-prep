# O(nlog(n)) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    total_speed = 0

    if fastest:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
        blueShirtSpeeds.reverse()

        for i in range(len(redShirtSpeeds)):
            total_speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()

        for i in range(len(redShirtSpeeds)):
            total_speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return total_speed
