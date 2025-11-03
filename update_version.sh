#!/bin/bash

# 简化的版本更新脚本
# 用法: ./update_version.sh [patch|minor|major] [commit_message]

# 颜色输出
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# 默认参数
UPDATE_TYPE=${1:-patch}
COMMIT_MSG=${2:-"版本更新"}

echo -e "${BLUE}🔄 BlenderRenderNanoBanana 版本更新器${NC}"
echo "================================================"

# 检查git状态
if ! git diff --quiet; then
    echo -e "${YELLOW}⚠️  检测到未提交的更改${NC}"
    git status --short
    read -p "是否继续? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 0
    fi
fi

# 读取当前版本
VERSION_LINE=$(grep '"version":' BlenderRenderNanoBanana/__init__.py)
if [[ $VERSION_LINE =~ \(([0-9]+),\ ([0-9]+),\ ([0-9]+)\) ]]; then
    MAJOR=${BASH_REMATCH[1]}
    MINOR=${BASH_REMATCH[2]}
    PATCH=${BASH_REMATCH[3]}
    
    echo -e "${BLUE}📋 当前版本: v${MAJOR}.${MINOR}${PATCH}${NC}"
    
    # 计算新版本
    case $UPDATE_TYPE in
        "major")
            MAJOR=$((MAJOR + 1))
            MINOR=0
            PATCH=0
            ;;
        "minor")
            MINOR=$((MINOR + 1))
            PATCH=0
            ;;
        "patch"|*)
            PATCH=$((PATCH + 1))
            ;;
    esac
    
    NEW_VERSION="v${MAJOR}.${MINOR}${PATCH}"
    echo -e "${GREEN}📈 新版本: ${NEW_VERSION}${NC}"
else
    echo -e "${RED}❌ 无法解析当前版本${NC}"
    exit 1
fi

# 更新__init__.py中的版本号
sed -i '' "s/\"version\": ([0-9]*, [0-9]*, [0-9]*)/\"version\": (${MAJOR}, ${MINOR}, ${PATCH})/" BlenderRenderNanoBanana/__init__.py

echo -e "${BLUE}📝 已更新版本号到 ${NEW_VERSION}${NC}"

# 创建发布包
echo -e "${BLUE}📦 创建发布包...${NC}"
./create_release.sh

# Git操作
echo -e "${BLUE}📤 提交到Git...${NC}"
git add .
git commit -m "${NEW_VERSION}: ${COMMIT_MSG}"
git tag "${NEW_VERSION}" -m "版本 ${NEW_VERSION} - ${COMMIT_MSG}"

read -p "是否推送到GitHub? (Y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Nn]$ ]]; then
    echo -e "${YELLOW}⏸️  跳过推送，请手动运行: git push origin main --tags${NC}"
else
    git push origin main --tags
    echo -e "${GREEN}✅ 已推送到GitHub${NC}"
fi

echo -e "\n${GREEN}🎉 版本更新完成！${NC}"
echo -e "${BLUE}📋 摘要:${NC}"
echo "   - 版本: ${NEW_VERSION}"
echo "   - 发布包: releases/BlenderRenderNanoBanana_${NEW_VERSION}.zip"
echo "   - Git标签: ${NEW_VERSION}"