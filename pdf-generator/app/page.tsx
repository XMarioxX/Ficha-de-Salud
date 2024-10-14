"use client";
import { Input } from "@nextui-org/input";
import { useState } from "react";
import { Button } from "@nextui-org/button";
import { Tabs, Tab } from "@nextui-org/tabs";
import axios from "axios";

export default function Home() {
  const [nombre, setNombre] = useState("");
  const [provincia, setProvincia] = useState("");
  const [cum, setCum] = useState("");
  const [fechaNacimiento, setFechaNacimiento] = useState("");
  const [grupo, setGrupo] = useState("");
  const [seccion, setSeccion] = useState("");
  const [alerta, setAlerta] = useState("-");

  const [grupoRH, setGrupoRH] = useState("");
  const [peso, setPeso] = useState("");
  const [talla, setTalla] = useState("");
  const [imc, setImc] = useState("");
  const [alimentacion, setAlimentacion] = useState("");
  const [nombreProveedorInstituciones, setNombreProveedorInstituciones] = useState("");
  const [numeroPolizaInstituciones, setNumeroPolizaInstituciones] = useState("");
  const [derechoHabienciaInstituciones, setDerechoHabienciaInstituciones] = useState("");
  const [observacionesInstituciones, setObservacionesInstituciones] = useState("");
  const [nombreProveedorAseguradoras, setNombreProveedorAseguradoras] = useState("");
  const [numeroPolizaAseguradoras, setNumeroPolizaAseguradoras] = useState("");
  const [derechoHabienciaAseguradoras, setDerechoHabienciaAseguradoras] = useState("");
  const [observacionesAseguradoras, setObservacionesAseguradoras] = useState("");
  const [nombreProveedorParticular, setNombreProveedorParticular] = useState("");
  const [numeroPolizaParticular, setNumeroPolizaParticular] = useState("");
  const [derechoHabienciaParticular, setDerechoHabienciaParticular] = useState("");
  const [observacionesParticular, setObservacionesParticular] = useState("");


  const handleSubmit = async (e: { preventDefault: () => void; }) => {
    e.preventDefault();

    const data = {
      nombre,provincia,cum,fecha_nacimiento: fechaNacimiento,grupo,seccion,alerta,
      grupoRH,peso,talla,imc,alimentacion,nombreProveedorInstituciones,numeroPolizaInstituciones
    };

    try {
      const response = await axios.post("http://localhost:8000/api/ficha-medica/", data);
      console.log("Respuesta de la API:", response.data);
    } catch (error) {
      console.error("Error al enviar los datos:", error);
    }
  };

  const isFormValid = () => {
    return (
      nombre &&
      provincia &&
      cum &&
      fechaNacimiento &&
      grupo &&
      seccion
    );
  };

  return (
    <>
      <h2 className="text-4xl font-semibold text-center">Ficha Médica</h2>
      <div className="flex items-center justify-center min-h-screen p-4">
        <form onSubmit={handleSubmit} className="rounded-lg shadow-md p-8 space-y-4 w-full max-w-md">
          <Tabs aria-label="Options">
            <Tab key="datos_Identificacion" title="Datos Identificación">
              <div className="space-y-4">
                <Input
                  type="text"
                  label="Nombre Completo"
                  value={nombre}
                  onChange={(e) => setNombre(e.target.value)}
                  required
                  className="w-full"
                  isRequired={true}
                />
                <Input
                  type="text"
                  label="Provincia"
                  value={provincia}
                  onChange={(e) => setProvincia(e.target.value)}
                  required
                  className="w-full"
                  isRequired={true}
                />
                <Input
                  type="text"
                  label="CUM"
                  value={cum}
                  onChange={(e) => setCum(e.target.value)}
                  required
                  className="w-full"
                  isRequired={true}
                />
                <Input
                  type="date"
                  label="Fecha de Nacimiento"
                  value={fechaNacimiento}
                  onChange={(e) => setFechaNacimiento(e.target.value)}
                  required
                  className="w-full"
                  isRequired={true}
                />
                <Input
                  type="text"
                  label="Grupo"
                  value={grupo}
                  onChange={(e) => setGrupo(e.target.value)}
                  required
                  className="w-full"
                  isRequired={true}
                />
                <Input
                  type="text"
                  label="Sección"
                  value={seccion}
                  onChange={(e) => setSeccion(e.target.value)}
                  required
                  className="w-full"
                  isRequired={true}
                />
                <Input
                  type="text"
                  label="Alerta"
                  value={alerta}
                  onChange={(e) => setAlerta(e.target.value)}
                  required
                  className="w-full"
                />
              </div>
            </Tab>
            <Tab key="datos_Medicos" title="Datos Médicos">
              <div className="space-y-4">
                <Input
                  type="text"
                  label="Grupo y RH"
                  value={nombre}
                  onChange={(e) => setNombre(e.target.value)}
                  required
                  className="w-full"
                  isRequired={true}
                />
              </div>
            </Tab>
            <Tab key="videos" title="Videos"></Tab>
          </Tabs>
          <Button
            type="submit"
            color="primary"
            className="w-full"
            isDisabled={!isFormValid()}
          >
            Enviar
          </Button>
        </form>
      </div>
    </>
  );
}
