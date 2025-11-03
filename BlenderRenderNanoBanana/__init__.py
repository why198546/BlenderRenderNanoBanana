"""
Nano Banana AI Renderer - Blender plugin for Google Gemini 2.5 Flash Image
"""

bl_info = {
    "name": "Nano Banana AI Renderer",
    "author": "Assistant",
    "version": (1, 3, 8),
    "blender": (3, 0, 0),
    "location": "Render Properties > Nano Banana Renderer",
    "description": "AI-powered rendering using Google Gemini 2.5 Flash Image",
    "category": "Render",
}

import bpy
import os
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import StringProperty, BoolProperty, IntProperty, FloatProperty, EnumProperty

# Import all modules
from . import properties
from . import operators
from . import panels

# Test operator for debugging
class NANOBANANA_OT_test_render(Operator):
    """测试渲染按钮是否工作"""
    bl_idname = "nano_banana.test_render"
    bl_label = "Test Render"
    bl_description = "Test if render button works"
    
    def execute(self, context):
        print("=== 测试渲染按钮被点击了！===")
        self.report({'INFO'}, "TEST: Render button clicked!")
        
        # 测试基本功能
        print("1. 检查API密钥...")
        props = context.scene.nano_banana
        if props.api_key:
            print(f"API密钥存在: {props.api_key[:10]}...")
            self.report({'INFO'}, "API key found")
        else:
            print("API密钥不存在")
            self.report({'WARNING'}, "No API key")
        
        print("2. 检查提示词...")
        if props.prompt:
            print(f"提示词: {props.prompt}")
            self.report({'INFO'}, f"Prompt: {props.prompt}")
        else:
            print("提示词为空")
            self.report({'WARNING'}, "No prompt")
        
        print("3. 创建测试图像...")
        try:
            # 创建一个简单的测试图像
            image = bpy.data.images.new("NanoBanana_Test", width=512, height=512)
            
            # 创建渐变测试图像
            pixels = []
            for y in range(512):
                for x in range(512):
                    # 简单的渐变模式
                    r = x / 512.0
                    g = y / 512.0
                    b = 0.5
                    a = 1.0
                    pixels.extend([r, g, b, a])
            
            image.pixels = pixels
            
            # 在图像编辑器中显示
            for area in context.screen.areas:
                if area.type == 'IMAGE_EDITOR':
                    for space in area.spaces:
                        if space.type == 'IMAGE_EDITOR':
                            space.image = image
                            break
                    break
            
            print("✅ 测试图像创建成功！")
            self.report({'INFO'}, "Test image created successfully!")
            
        except Exception as e:
            print(f"❌ 创建测试图像失败: {e}")
            self.report({'ERROR'}, f"Failed to create test image: {e}")
        
        print("4. 测试渲染图像生成...")
        try:
            # 使用默认渲染功能生成图像
            print("保存当前渲染设置...")
            original_filepath = context.scene.render.filepath
            original_file_format = context.scene.render.image_settings.file_format
            original_x = context.scene.render.resolution_x
            original_y = context.scene.render.resolution_y
            
            # 设置渲染参数
            context.scene.render.resolution_x = 512
            context.scene.render.resolution_y = 512
            
            # 确保场景中有可渲染的内容
            print("检查场景内容...")
            
            # 检查现有场景内容
            print("=== 详细场景分析 ===")
            
            # 强制设置渲染引擎
            original_engine = context.scene.render.engine
            try:
                context.scene.render.engine = 'BLENDER_EEVEE_NEXT'
                print("✅ 设置渲染引擎为 EEVEE_NEXT")
            except:
                try:
                    context.scene.render.engine = 'BLENDER_EEVEE'
                    print("✅ 设置渲染引擎为 EEVEE")
                except:
                    context.scene.render.engine = 'CYCLES'
                    print("✅ 设置渲染引擎为 CYCLES")
            
            print(f"当前渲染引擎: {context.scene.render.engine}")
            
            # 检查摄像机
            if context.scene.camera:
                cam = context.scene.camera
                print(f"✅ 摄像机: {cam.name} 位置: {cam.location}")
            else:
                print("❌ 没有摄像机，添加默认摄像机...")
                bpy.ops.object.camera_add(location=(7.48, -6.51, 5.34))
                context.scene.camera = context.object
                print("✅ 已添加摄像机")
            
            # 检查灯光
            lights = [obj for obj in context.scene.objects if obj.type == 'LIGHT']
            if lights:
                print(f"✅ 灯光: {len(lights)} 个")
                for light in lights:
                    print(f"  - {light.name}: {light.data.type}, 能量: {light.data.energy}")
            else:
                print("❌ 没有灯光，添加强光源...")
                bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
                sun = context.object
                sun.data.energy = 10.0
                print("✅ 已添加太阳光")
            
            # 详细检查所有对象
            all_objects = list(context.scene.objects)
            visible_meshes = [obj for obj in all_objects if obj.type == 'MESH' and obj.visible_get()]
            print(f"场景总对象数: {len(all_objects)}")
            print(f"可见网格对象: {len(visible_meshes)}")
            
            for obj in all_objects[:5]:  # 显示前5个对象
                visibility = "可见" if obj.visible_get() else "隐藏"
                print(f"  - {obj.name} ({obj.type}): {visibility}")
            
            if not visible_meshes:
                print("❌ 没有可见对象，添加测试立方体...")
                bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), size=3)
                cube = context.object
                # 添加明亮材质
                mat = bpy.data.materials.new(name="BrightTestMaterial")
                cube.data.materials.append(mat)
                mat.use_nodes = True
                bsdf = mat.node_tree.nodes["Principled BSDF"]
                bsdf.inputs[0].default_value = (1.0, 0.0, 0.0, 1.0)  # 纯红色
                bsdf.inputs[7].default_value = 0.0  # 完全光滑
                print("✅ 已添加红色测试立方体")
            
            # 强制更新场景
            context.view_layer.update()
            bpy.context.evaluated_depsgraph_get().update()
            print("✅ 场景已更新")
            
            # 设置临时输出路径
            import tempfile
            temp_dir = tempfile.gettempdir()
            temp_image_path = os.path.join(temp_dir, "blender_render_temp.png")
            
            context.scene.render.filepath = temp_image_path
            context.scene.render.image_settings.file_format = 'PNG'
            
            print("执行默认渲染...")
            bpy.ops.render.render(write_still=True)
            
            # 检查文件是否生成
            if os.path.exists(temp_image_path):
                print(f"✅ 渲染图像已保存到: {temp_image_path}")
                
                # 将保存的图像加载到Blender中
                viewport_image = bpy.data.images.load(temp_image_path)
                viewport_image.name = "Viewport_Capture_Test"
                
                print(f"✅ 图像已加载到Blender: {viewport_image.name}, 尺寸: {viewport_image.size}")
                print("✅ 渲染图像生成测试成功！")
                self.report({'INFO'}, "Render image generation test successful!")
                
                # 清理临时文件
                try:
                    os.remove(temp_image_path)
                    print("✅ 临时文件已清理")
                except:
                    print("⚠️ 临时文件清理失败，但不影响功能")
                
            else:
                print("❌ 渲染文件未生成")
                self.report({'WARNING'}, "Render file not generated")
            
            # 恢复原始设置
            context.scene.render.filepath = original_filepath
            context.scene.render.image_settings.file_format = original_file_format
            context.scene.render.resolution_x = original_x
            context.scene.render.resolution_y = original_y
            
        except Exception as e:
            print(f"❌ 渲染测试失败: {e}")
            self.report({'WARNING'}, f"Render test failed: {str(e)}")
        
        print("=== 测试完成！===")
        return {'FINISHED'}

# Registration
classes = (
    properties.NanoBananaProperties,
    operators.NANOBANANA_OT_api_key_dialog,
    operators.NANOBANANA_OT_setup_api,
    # operators.NANOBANANA_OT_capture_viewport,  # 暂时禁用以解决导入问题
    operators.NANOBANANA_OT_render_viewport,  # 主要的渲染operator
    operators.NANOBANANA_OT_render_animation,
    operators.NANOBANANA_OT_save_image,  # 保存图片操作符
    operators.NANOBANANA_OT_view_in_editor,  # 在图像编辑器中查看操作符
    NANOBANANA_OT_test_render,
    panels.NANOBANANA_PT_render_panel,  # 渲染属性面板
    panels.NANOBANANA_PT_viewport_panel,  # 3D视口面板
    panels.NANOBANANA_PT_sidebar_panel,  # 侧边栏面板
)

def register():
    print("Registering Nano Banana Renderer...")
    
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
            print(f"Registered: {cls.__name__}")
        except Exception as e:
            print(f"Failed to register {cls.__name__}: {e}")
    
    bpy.types.Scene.nano_banana = bpy.props.PointerProperty(type=properties.NanoBananaProperties)
    
    # 自动加载已保存的API key
    try:
        from .properties import load_api_key
        saved_api_key = load_api_key()
        if saved_api_key:
            # 需要在场景创建后设置，使用定时器
            bpy.app.timers.register(lambda: set_saved_api_key(saved_api_key), first_interval=0.1)
            print(f"Found saved API key: {saved_api_key[:10]}...")
        else:
            print("No saved API key found")
    except Exception as e:
        print(f"Failed to load saved API key: {e}")
    
    print("Nano Banana Renderer registered successfully!")

def set_saved_api_key(api_key):
    """Set the saved API key to the current scene properties"""
    try:
        if bpy.context.scene and hasattr(bpy.context.scene, 'nano_banana'):
            bpy.context.scene.nano_banana.api_key = api_key
            print(f"API key loaded successfully: {api_key[:10]}...")
            return None  # Remove timer
    except Exception as e:
        print(f"Failed to set API key: {e}")
    
    # Return timer function to try again if failed
    return 0.1

def unregister():
    print("Unregistering Nano Banana Renderer...")
    
    if hasattr(bpy.types.Scene, 'nano_banana'):
        del bpy.types.Scene.nano_banana
    
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass
    
    print("Nano Banana Renderer unregistered successfully!")

if __name__ == "__main__":
    register()
