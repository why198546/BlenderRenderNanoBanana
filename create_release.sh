#!/bin/bash

# BlenderRenderNanoBanana Release Creation Script
# 直接在releases目录中创建压缩包，避免重复文件

# 颜色输出
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🍌 BlenderRenderNanoBanana Release Creator${NC}"
echo "================================================"

# 检查是否在正确的目录
if [ ! -d "BlenderRenderNanoBanana" ]; then
    echo -e "${RED}❌ 错误: 请在包含BlenderRenderNanoBanana目录的根目录运行此脚本${NC}"
    exit 1
fi

# 读取当前版本号
if [ ! -f "BlenderRenderNanoBanana/__init__.py" ]; then
    echo -e "${RED}❌ 错误: 找不到__init__.py文件${NC}"
    exit 1
fi

# 从__init__.py提取版本号
VERSION_LINE=$(grep '"version":' BlenderRenderNanoBanana/__init__.py)
if [[ $VERSION_LINE =~ \(([0-9]+),\ ([0-9]+),\ ([0-9]+)\) ]]; then
    MAJOR=${BASH_REMATCH[1]}
    MINOR=${BASH_REMATCH[2]}
    PATCH=${BASH_REMATCH[3]}
    VERSION="v${MAJOR}.${MINOR}${PATCH}"
    echo -e "${BLUE}📋 检测到版本: ${VERSION}${NC}"
else
    echo -e "${RED}❌ 错误: 无法解析版本号${NC}"
    exit 1
fi

# 确保releases目录存在
mkdir -p releases

# 压缩包文件名
ZIP_NAME="BlenderRenderNanoBanana_${VERSION}.zip"
ZIP_PATH="releases/${ZIP_NAME}"

# 检查文件是否已存在
if [ -f "$ZIP_PATH" ]; then
    echo -e "${YELLOW}⚠️  文件已存在: ${ZIP_PATH}${NC}"
    read -p "是否覆盖? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}❌ 取消创建${NC}"
        exit 0
    fi
    rm "$ZIP_PATH"
fi

# 创建压缩包 (直接在releases目录中)
echo -e "${BLUE}📦 创建压缩包: ${ZIP_NAME}${NC}"
cd releases
zip -r "${ZIP_NAME}" ../BlenderRenderNanoBanana/
cd ..

# 检查创建结果
if [ -f "$ZIP_PATH" ]; then
    FILE_SIZE=$(ls -lh "$ZIP_PATH" | awk '{print $5}')
    echo -e "${GREEN}✅ 成功创建: ${ZIP_PATH} (${FILE_SIZE})${NC}"
    
    # 显示releases目录内容
    echo -e "\n${BLUE}📁 Releases目录内容:${NC}"
    ls -la releases/*.zip | tail -5  # 显示最新的5个文件
    
    echo -e "\n${GREEN}🎉 发布包创建完成！${NC}"
    echo -e "${YELLOW}💡 下一步操作:${NC}"
    echo "   1. 更新README.md中的下载链接"
    echo "   2. 更新releases/README.md"
    echo "   3. git add . && git commit && git tag && git push"
else
    echo -e "${RED}❌ 压缩包创建失败${NC}"
    exit 1
fi