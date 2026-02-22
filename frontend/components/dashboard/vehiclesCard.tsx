"use client";

import type { Vehicle } from "@/lib/types";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { VehicleQrDialog } from "./vehicleQrDialog";
import { Button } from "@/components/ui/button";
import { useState } from "react";

export function VehiclesCard({ vehicles }: { vehicles: Vehicle[] }) {
  const [qrFor, setQrFor] = useState<Vehicle | null>(null);

  return (
    <Card>
      <CardHeader>
        <CardTitle>Vehicles</CardTitle>
      </CardHeader>
      <CardContent className="space-y-3">
        {vehicles.length === 0 ? (
          <div className="text-sm text-muted-foreground">
            No vehicles yet. Add one.
          </div>
        ) : (
          vehicles.map((v, idx) => (
            <div key={v.id} className="space-y-2">
              <div className="flex items-center justify-between">
                <div>
                  <div className="font-medium">{v.label}</div>
                  {v.plate_last4 ? (
                    <div className="text-xs text-muted-foreground">
                      Plate: ****{v.plate_last4}
                    </div>
                  ) : null}
                </div>
                <Button variant="outline" onClick={() => setQrFor(v)}>
                  QR
                </Button>
              </div>
              {idx !== vehicles.length - 1 ? <Separator /> : null}
            </div>
          ))
        )}

        <VehicleQrDialog vehicle={qrFor} onClose={() => setQrFor(null)} />
      </CardContent>
    </Card>
  );
}
