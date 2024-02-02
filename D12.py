#D12
import bpy
from math import radians
bpy.ops.preferences.addon_enable(module = "add_mesh_extra_objects")

NUMBERS = {
    0: [None] * 12,
    1: [1, 8, 11, 14, 19, 22, 27, 30, 35, 38, 41, 48],
    2: [2, 7, 10, 15, 18, 23, 26, 31, 34, 39, 42, 47],
    3: [3, 6, 12, 13, 17, 24, 25, 32, 36, 37, 43, 46],
    4: [4, 5, 9,  16, 20, 21, 28, 29, 33, 40, 44, 45],
}


def pathify(path, name):
    splitFilepath = path.split("\\")
    newFilepath = ""
    if len(splitFilepath) > 1:
        for i in splitFilepath:
            newFilepath += i + "/"
    else:
        newFilepath = splitFilepath[0] + "/"
    if newFilepath[-1] == "/" and newFilepath[-2] == "/":
        newFilepath = newFilepath[0:-1]
    newFilepath += name
    return newFilepath


def stamp():
    obj = bpy.context.scene.objects["die"]
    bpy.data.objects['Text'].select_set(False)
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
    bpy.ops.object.modifier_apply(modifier = "Boolean")


def deleteNum():
    obj = bpy.context.scene.objects["Text"]
    bpy.data.objects['die'].select_set(False)
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.delete()


def makeNum(number, font, scale):
    bpy.ops.object.text_add(enter_editmode = False, align = 'WORLD', location = (0, 0, 0), scale = (1, 1, 1))
    num = bpy.context.active_object
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type = 'PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type = 'PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type = 'PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type = 'PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text = str(number))
    bpy.ops.object.editmode_toggle()
    bpy.data.objects["Text"].data.font = bpy.data.fonts.load(font)
    bpy.ops.object.convert(target = 'MESH')
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action = "SELECT")
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region = {"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate = {"value":(0, 0, 49.5538), "orient_type":'NORMAL', "orient_matrix":((0, -1, 0), (1, 0, -0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
    bpy.ops.object.editmode_toggle()
    num.scale = [10 * scale, 10 * scale, 0.1]
    bpy.ops.object.origin_set(type = 'ORIGIN_CENTER_OF_VOLUME', center = 'MEDIAN')
    num.location = [0, 0, 9.75]
    return num


def make(digit, font, scale):
    if digit is not None:
        _make(digit, font, scale)
        if (digit == 6) or (digit == 9):
            _make("_", font, scale)


def _make(digit, font, scale):
    num = makeNum(digit, font, scale)
    if digit == "_":
        num.location[1] -= scale * 4
    bpy.data.objects["die"].select_set(True)
    stamp()
    deleteNum()



ORIGINAL_ORDER = [6,1,4,3,11,8,7,5,2,10,9,12]

def makeD12(fontFolder, fontName, outputFolder, scale, index, numbers):
    numbers = [numbers[x-1] for x in ORIGINAL_ORDER]


    bpy.ops.mesh.primitive_solid_add(source='12')
    die = bpy.context.active_object

    bevel_mod = die.modifiers.new("mod", 'BEVEL')
    bevel_mod.width = 0.03
    bevel_mod.segments = 8
    bpy.ops.object.modifier_apply(modifier = "mod")

    die.name = "die"
    #rotate
    die.rotation_euler[0] = radians(-58.285)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    #scale
    die.dimensions[2] = 18.5
    die.scale[0] = die.scale[2]
    die.scale[1] = die.scale[2]
    font = pathify(fontFolder, fontName)
    make(numbers[0], font, scale)
    die.select_set(True)
    die.rotation_euler[2] = radians(36)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    die.rotation_euler[0] = radians(63.43)
    make(numbers[1], font, scale)
    die.select_set(True)
    die.rotation_euler[0] = 0
    die.rotation_euler[2] = radians(72)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    die.rotation_euler[0] = radians(63.43)
    make(numbers[2], font, scale)
    die.select_set(True)
    die.rotation_euler[0] = 0
    die.rotation_euler[2] = radians(72)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    die.rotation_euler[0] = radians(63.43)
    make(numbers[3], font, scale)
    die.select_set(True)
    die.rotation_euler[0] = 0
    die.rotation_euler[2] = radians(72)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    die.rotation_euler[0] = radians(63.43)
    make(numbers[4], font, scale)
    die.select_set(True)
    die.rotation_euler[0] = 0
    die.rotation_euler[2] = radians(72)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    die.rotation_euler[0] = radians(63.43)
    make(numbers[5], font, scale)
    die.select_set(True)
    die.rotation_euler[0] = 0
    die.rotation_euler[2] = radians(36)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    die.rotation_euler[0] = radians(180)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    make(numbers[6], font, scale)
    die.select_set(True)
    die.rotation_euler[2] = radians(36)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    die.rotation_euler[0] = radians(63.43)
    make(numbers[7], font, scale)
    die.select_set(True)
    die.rotation_euler[0] = 0
    die.rotation_euler[2] = radians(72)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    die.rotation_euler[0] = radians(63.43)
    make(numbers[8], font, scale)
    die.select_set(True)
    die.rotation_euler[0] = 0
    die.rotation_euler[2] = radians(72)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    die.rotation_euler[0] = radians(63.43)
    make(numbers[9], font, scale)
    die.select_set(True)
    die.rotation_euler[0] = 0
    die.rotation_euler[2] = radians(72)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    die.rotation_euler[0] = radians(63.43)
    make(numbers[10], font, scale)
    die.select_set(True)
    die.rotation_euler[0] = 0
    die.rotation_euler[2] = radians(72)
    bpy.ops.object.transform_apply(location = False, rotation = True, scale = False)
    die.rotation_euler[0] = radians(63.43)
    make(numbers[11], font, scale)
    bpy.ops.export_mesh.stl(filepath=pathify(outputFolder, "D12_" + str(index) + ".stl"))


if __name__ == "__main__":
    # Edit these to change font and destination

    systemFontFolderPath = "/System/Library/Fonts/Supplemental"
    chosenFontNameAndExtension = "Arial Rounded Bold.ttf"
    outputDestinationFolder = "./output"
    numScale = 1
    for idx, numbers in NUMBERS.items():
        while bpy.data.objects:
            bpy.data.objects.remove(bpy.data.objects[0], do_unlink=True)
        print("Working on", idx)
        makeD12(systemFontFolderPath, chosenFontNameAndExtension, outputDestinationFolder, numScale, idx, numbers)
