# 🛠️ 开发工具脚本

这个目录包含用于BlenderRenderNanoBanana项目开发和发布的便捷脚本。

## 📜 脚本列表

### 🚀 create_release.sh
**用途**: 直接在releases目录中创建发布压缩包，避免根目录重复文件

**使用方法**:
```bash
./create_release.sh
```

**功能**:
- ✅ 自动检测当前版本号（从`__init__.py`）
- ✅ 直接在`releases/`目录创建压缩包
- ✅ 文件大小显示和重复检查
- ✅ 彩色输出和进度提示

---

### 🔄 update_version.sh  
**用途**: 自动化版本更新、发布包创建和Git操作

**使用方法**:
```bash
# 补丁版本更新 (1.3.8 → 1.3.9)
./update_version.sh patch "修复xxx问题"

# 小版本更新 (1.3.8 → 1.4.0)  
./update_version.sh minor "新增xxx功能"

# 大版本更新 (1.3.8 → 2.0.0)
./update_version.sh major "重大重构"

# 默认补丁更新
./update_version.sh
```

**功能**:
- ✅ 自动更新版本号
- ✅ 创建发布压缩包
- ✅ Git提交和标签创建
- ✅ 可选择是否推送到GitHub
- ✅ 完整的操作摘要

---

## 🎯 典型工作流程

### 1. 日常开发更新
```bash
# 修改代码...
./update_version.sh patch "修复弹出窗口大小问题"
```

### 2. 功能更新
```bash  
# 添加新功能...
./update_version.sh minor "新增批量渲染功能"
```

### 3. 手动发布
```bash
# 仅创建发布包，不更新版本
./create_release.sh
```

---

## 📋 注意事项

1. **脚本位置**: 必须在项目根目录运行
2. **Git状态**: update_version.sh会检查未提交的更改
3. **文件覆盖**: create_release.sh会询问是否覆盖已存在的文件
4. **自动推送**: update_version.sh可以选择是否自动推送到GitHub

---

## 🎨 输出样式

脚本使用彩色输出来提高可读性：
- 🔵 **蓝色**: 信息和进度
- 🟢 **绿色**: 成功操作
- 🟡 **黄色**: 警告和提示
- 🔴 **红色**: 错误信息

---

## 🔧 故障排除

### 权限问题
```bash
chmod +x *.sh
```

### 版本号解析失败
检查`BlenderRenderNanoBanana/__init__.py`中的版本格式：
```python
"version": (1, 3, 8),
```

### Git推送失败
手动推送：
```bash
git push origin main --tags
```