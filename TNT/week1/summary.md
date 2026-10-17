## Day1
## Day2
```

┌──────────────────────────────────────────────────────────────────────────────┐
│  TOOL   │ PRIMARY USE CASE               │ UNIQUE EXAM TRAP / MECHANISM      │
├─────────┼────────────────────────────────┼───────────────────────────────────┤
│ cat     │ Stream/concatenate files       │ -n numbers all; -b numbers non-   │
│         │                                │ blank; -s squeezes empty lines.   │
│ tac     │ Invert line order (bottom-up)  │ Reverses lines, NOT characters.   │
│ rev     │ Invert characters horizontally │ Reverses characters, NOT lines.   │
│ head    │ View top of file               │ head -n -K drops last K lines.    │
│ tail    │ View bottom / stream live logs │ tail -n +K starts at line K.      │
│         │                                │ tail -F follows logrotate renames.│
│ less    │ Interactive terminal pager     │ Lazy loads chunks; fast on 50GB.  │
│ wc      │ Count metrics                  │ wc -l counts '\n', not rows.      │
│         │                                │ -c counts bytes, -m counts chars. │
│ file    │ Determine file type            │ Ignores extensions; inspects magic│
│         │                                │ bytes; -L follows symlinks.       │
└──────────────────────────────────────────────────────────────────────────────┘

```