# cordova-icon

> 生成Cordova项目的各种尺寸icon

## 原始icon

根目录下的`logo.png`，如果需要修改位置，请修改`run.py`中的

```python
logo = Image.open('logo.png')
```

## 配置生成icon名称和尺寸

修改`app`目录下的`icon.ini`

```ini
[icon]
icon-36-ldpi = (36,36)
icon-48-mdpi = (48,48)
icon-72-hdpi = (72,72)
icon-96-xhdpi = (96,96)
icon-144-xxhdpi = (144,144)
icon-192-xxxhdpi = (192,192)
```

> 注意: 尺寸使用元组的字符串表示形式 (x, y)

## 运行

准备环境

```bash
python3.6 -m venv venv
source venv/bin/activate
```

```bash
(venv) ➜  cordova-icon git:(develop) ✗ python3 run.py
start!
done!
```
