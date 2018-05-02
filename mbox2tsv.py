#!/usr/bin/env python3

import sys
import mailbox

def cellify(s):
    lines = []
    for L in s.splitlines():
        L = L.strip()
        if L.startswith('>'): continue
        if L.startswith('On ') and L.endswith('> wrote:'): continue
        if L.startswith('----') and 'Forwarded' in L: continue
        lines.append(L)
    return ' '.join(lines)

def main(fn):
    mbox = mailbox.mbox(fn)
    print('\t'.join(['date', 'from', 'to', 'subject', 'content']))
    for msgid, msg in mbox.iteritems():
        f = msg['From'] or ''
        t = msg['To'] or ''
        d = msg['Date'] or ''
        s = msg['Subject'] or ''
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                payload = part.get_payload(decode=True) or ''
                print('\t'.join([d, cellify(f), cellify(t), cellify(s), cellify(payload.decode('utf-8'))]))

main(sys.argv[1])
