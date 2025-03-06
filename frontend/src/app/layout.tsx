import type { Metadata } from "next";
import { Geist, Geist_Mono, Inter } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});
// Manfred the woke gentleman - dog

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

const inter = Inter({
  variable: "--inter",
  subsets: ["latin"],
})
// At my last job, we had a huge data model represented as 
// a tree where most of the nodes were immutable but some were 
// mutable and we wanted the immutable ones to be not copied at 
// all (just return the reference) and the others to be recursively 
// copied, so I made an @immutable decorator that could be used to abort 
// copying / deep copying, and it worked very well and drastically reduced 
// memory use and increased performance
//https://www.youtube.com/shorts/vibK3FyzWvU
export const metadata: Metadata = {
  title: "MenuShare | Home",
  description: "MenuShare application",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${inter.variable} antialiased`}
      >
        <main className="menu-container">{children}</main> 
      </body>
    </html>
  );
}
