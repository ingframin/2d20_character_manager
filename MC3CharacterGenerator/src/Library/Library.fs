module Library

open System.Text.Json

type AttributeName = | Strength | Physique | Agility | Awareness | Coordination | Intelligence | Mental | Personality

type Career = {roll: int; career: string; attribs: Map<AttributeName, int>; mandatory_skills: string list; elective_skills: string list; talents: string list; equipment: string list}

type Attribute = {name: AttributeName; value: int} 
type Skill = {name:string; expertise: int; focus: int; parent:AttributeName}


let getJson value =
    let json = JsonSerializer.Serialize(value)
    value, json