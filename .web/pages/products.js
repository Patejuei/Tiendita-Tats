import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import range from "/utils/helpers/range.js"
import "focus-visible/dist/focus-visible"
import { Box, HStack, Link, Menu, MenuItem, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Spacer, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <VStack alignItems={`flex-start`} sx={{"transition": "left 0.5s, width 0.5s", "position": "relative"}}>
  <HStack sx={{"backgroundColor": "#EBD3B5", "width": "100%"}}>
  <Menu>
  <Link as={NextLink} href={`/`} sx={{"color": "#404040", "backgroundColor": "#D9D8A9", "margin": "0.7rem 0.5rem", "padding": "0.2rem", "borderRadius": "1em", "border": "1px solid #C9F5D6"}}>
  <MenuItem>
  {`Inicio`}
</MenuItem>
</Link>
  <Link as={NextLink} href={`/products`} sx={{"color": "#404040", "backgroundColor": "#D9D8A9", "margin": "0.7rem 0.5rem", "padding": "0.2rem", "borderRadius": "1em", "border": "1px solid #C9F5D6"}}>
  <MenuItem>
  {`Productos`}
</MenuItem>
</Link>
  <Spacer/>
  <Link as={NextLink} href={`/login`} sx={{"color": "#404040", "backgroundColor": "#D9D8A9", "margin": "0.7rem 0.5rem", "padding": "0.2rem", "borderRadius": "1em", "border": "1px solid #C9F5D6"}}>
  <MenuItem>
  {`Iniciar Sesión`}
</MenuItem>
</Link>
  <Link as={NextLink} href={`#register`} sx={{"color": "#404040", "backgroundColor": "#D9D8A9", "margin": "0.7rem 0.5rem", "padding": "0.2rem", "borderRadius": "1em", "border": "1px solid #C9F5D6"}}>
  <MenuItem>
  {`Registrarse`}
</MenuItem>
</Link>
  <Link as={NextLink} href={`#carro`} sx={{"color": "#404040", "backgroundColor": "#D9D8A9", "margin": "0.7rem 0.5rem", "padding": "0.2rem", "borderRadius": "1em", "border": "1px solid #C9F5D6"}}>
  <MenuItem>
  {`Carro`}
</MenuItem>
</Link>
</Menu>
</HStack>
  <Box>
  <Box>
  <Box>
  <HStack>
  <VStack/>
  <Box/>
</HStack>
</Box>
</Box>
</Box>
</VStack>
  <NextHead>
  <title>
  {`Productos - Tiendita Tat's`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
  <meta content={`width=device-width, shrink-to-fit=no, initial-scale=1`} name={`viewport`}/>
</NextHead>
</Fragment>
  )
}
