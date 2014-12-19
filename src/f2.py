import subprocess


def action():
    res = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print res.communicate
    out, err = res.communicate()

    if res.returncode != 0:
        raise Exception(out)

    print out

    return out