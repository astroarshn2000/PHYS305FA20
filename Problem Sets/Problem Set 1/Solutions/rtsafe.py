
def rtsafe(func, xlow, xhigh, epsilon):
    """
    Root finding by combined bisection and Newton iteration;
    func must return f, df/dx at x
    desired root must be on [xlow, xhigh]
    """

    flow, df = func(xlow)
    fhigh, df = func(xhigh)
    assert flow*fhigh < 0

    # early termination: If it worked, just return!
    if abs(flow) <= epsilon: return xlow
    if abs(fhigh) <= epsilon: return xhigh

    # if bracketing values don't give flow<0, reverse them
    if flow>0: xlow, xhigh = xhigh, xlow

    xmid = 0.5*(xlow+xhigh)
    dxold = abs(xhigh-xlow)
    dx = dxold
    fmid, df = func(xmid)

    MAXINT = 50
    for i in range(MAXINT):
        # if newton will take us outside the range,
        # or if convergence is too slow, use bisection
        if ((xmid-xhigh)*df - fmid) * ((xmid-xlow)*df - fmid) > 0 or abs(2*fmid) > abs(dxold*df):
            dxold = dx
            dx = 0.5*(xhigh-xlow)
            xmid = xlow + dx
            if xlow == xmid: return xmid

        # otherwise use newton
        else:
            dxold = dx
            dx = fmid/df
            temp = xmid
            xmid -= dx
            # if adding the correction doesn't change xmid, return it;
            # we're as close as we can get
            if temp==xmid: return xmid

        # if we are close enough, return the result
        if abs(fmid) < epsilon or abs(dx) < epsilon: return xmid

        fmid, df = func(xmid)
        if fmid<0:
            # on left side of root, update xlow
            xlow = xmid
        else:
            # on right side of root, update xr
            xhigh = xmid

    print("rtsafe: no convergence in ", MAXINT, "iterations; returning 'None'")
    return None
