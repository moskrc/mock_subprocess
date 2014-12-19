import subprocess


def action():
    res = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, err = res.communicate()

    if res.returncode != 0:
        raise Exception(out)

    return out