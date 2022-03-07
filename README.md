``` 
                  ___               _      
                 |__ \             | |     
     ___ _____   __ ) |___ ___   __| | ___ 
    / __/ __\ \ / // // __/ _ \ / _` |/ _ \
   | (__\__ \\ V // /| (_| (_) | (_| |  __/
    \___|___/ \_/|____\___\___/ \__,_|\___|
                                           
```                                                               

⭐ Star us on GitHub — it helps!

[![repo-size](https://img.shields.io/github/languages/code-size/imacwink/csv2code?style=flat)](https://github.com/imacwink/csv2code/archive/main.zip) [![tag](https://img.shields.io/github/v/tag/imacwink/csv2code)](https://github.com/imacwink/csv2code/tags) [![license](https://img.shields.io/github/license/imacwink/csv2code)](LICENSE) 

## Introduction
> The purpose is to quickly generate code in multiple languages ​​through scripts and templates, such as: Lua, C++, Java, etc.

```console
.
├── CSharp
├── Csv2CSharp.py
├── Example
├── LICENSE
├── Numeric
│   ├── Entity
│   │   └── Entity.csv
│   └── Skill
│       └── Skill.csv
├── README.md
└── Template
    ├── TemplateClass.cs
    ├── TemplateCsvData.cs
    └── TemplateCsvDataManager.cs

13 directories, 31 files
```

## Environment
> The only thing you need is to support the Python environment, for example:

```console
macwink$ python --version
Python 2.7.18
```

## Usage

### First
> Execute the following command on the command line.

```console
macwink$ python Csv2CSharp.py 

System: Darwin
Path: /Users/macwink/workspace/work/unity/csv2code

Start...
 -- Skill.csv
 -- Entity.csv
Finish
```

### Second
> Check the CSharp directory and generate the following code.

```console
macwink$ tree
.
├── CsvData.cs
├── CsvDataManager.cs
└── Model
    ├── Entity.cs
    └── Skill.cs

1 directory, 4 files
```

### Go on
> Copy the generated CSharp folder to the Unity project and write a simple test script to test.

```csharp
Entity csvEntity = (Entity)CsvDataManager.getInstance("Entity");
for (int i = 0; i < csvEntity.num(); i++)
{
    Debug.Log("ID : " + csvEntity.getInt(i, "id")
        + " | Name : " + csvEntity.get(i, "name")
        + " | Desc : " + csvEntity.get(i, "desc")
        + " | Speed : " + csvEntity.getFloat(i, "speed"));
}
```