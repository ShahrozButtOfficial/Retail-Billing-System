from cx_Freeze import setup,Executable,sys
includefiles=['icon.ico']
excludes=[]
packages=[]
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "Khaata Naama",
     "TARGETDIR",
     "[TARGETDIR]\main.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="1.2.0.5",
    description="Khaata Naama",
    author="Shahroz Butt Official",
    name="Billing System",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon='icon.ico',
        )
    ]
)